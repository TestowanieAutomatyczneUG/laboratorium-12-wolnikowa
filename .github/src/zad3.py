class MailServer:
    pass
class TemplateEngine:
    pass

class Messenger:
    def __init__(self):
        self.TemplateEngine = TemplateEngine()
        self.MailServer = MailServer()
    def sendMessage(self, address, message):
        if self.MailServer.sendMessage(address, message):
            return self.TemplateEngine.sendMessage(address, message)
        else:
            raise Exception('Fatal Error ')

    def receiveMessage(self):
        if self.MailServer.receiveMessage():
            return self.TemplateEngine.receiveMessage()
        else:
            raise Exception('Fatal Error ')


from unittest.mock import *
import unittest


class testMessenger(unittest.TestCase):
    def setUp(self):
        self.temp = Messenger()

    def test_messenger_send_error(self):
        MailServer = Mock()
        MailServer.sendMessage.return_value = False
        self.temp.MailServer = MailServer
        TemplateEngine = Mock()
        TemplateEngine.sendMessage.return_value = {'address': 'wiktoria@example.com', 'message': 'HelloWorld'}
        self.temp.TemplateEngine = TemplateEngine
        result = self.temp.sendMessage
        self.assertRaisesRegex(Exception, 'Fatal Error ', result, 'wiktoria@example.com', 'HelloWorld')

    def test_messenger_send_BAD_email(self):
        MailServer = Mock()
        MailServer.sendMessage.return_value = True
        self.temp.MailServer = MailServer
        TemplateEngine = Mock()
        TemplateEngine.sendMessage.side_effect = Exception("Bad email")
        self.temp.TemplateEngine = TemplateEngine
        result = self.temp.sendMessage
        self.assertRaisesRegex(Exception, 'Bad email', result, 'maciek_example.com', 'HelloWorld')

    def test_messenger_send(self):
        MailServer = Mock()
        TemplateEngine = Mock()
        MailServer.sendMessage.return_value = True
        self.temp.MailServer = MailServer
        TemplateEngine.sendMessage.return_value = {'address': 'wiktoria@example.com', 'message': 'HelloWorld'}
        self.temp.TemplateEngine = TemplateEngine
        result = self.temp.sendMessage('wiktoria@example.com', 'HelloWorld')
        self.assertEqual(result, {'address': 'wiktoria@example.com', 'message': 'HelloWorld'})

    def test_messenger_send_BAD_message(self):
        MailServer = Mock()
        MailServer.sendMessage.return_value = True
        self.temp.MailServer = MailServer
        TemplateEngine = Mock()
        TemplateEngine.sendMessage.side_effect = TypeError("Bad type message")
        self.temp.TemplateEngine = TemplateEngine
        result = self.temp.sendMessage
        self.assertRaisesRegex(Exception, "Bad type message", result, 'wiktoria@example.com', False)

    def test_messenger_receive_OK(self):
        MailServer = Mock()
        MailServer.receiveMessage.return_value = True
        self.temp.MailServer = MailServer
        TemplateEngine = Mock()
        TemplateEngine.receiveMessage.return_value = "HelloWorld"
        self.temp.TemplateEngine = TemplateEngine
        result = self.temp.receiveMessage()
        self.assertEqual(result, "HelloWorld")

    def test_messenger_receive_error(self):
        MailServer = Mock()
        MailServer.receiveMessage.return_value = False
        self.temp.MailServer = MailServer
        TemplateEngine = Mock()
        TemplateEngine.receiveMessage.return_value = "HelloWorld"
        self.temp.TemplateEngine = TemplateEngine
        result = self.temp.receiveMessage
        self.assertRaisesRegex(Exception, 'Fatal Error ', result)


if __name__ == '__main__':
    unittest.main()