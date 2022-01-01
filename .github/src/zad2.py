class Subscriber:
    def __init__(self):
        self.clients = []

    def add(self, name, email):
        for client in self.clients:
            if client["name"] == name and client["email"] == email:
                raise Exception("This client exists")
        if type(name) == str and type(email) == str:
            self.clients.append({"name": name, "email": email})
            return self.clients
        else:
            raise TypeError("Bad type name or/and email")

    def delete(self, name, email):
        for client in self.clients:
            if client["name"] == name and client["email"] == email:
                self.clients.remove({"name": name, "email": email})
                return "Delete: %s, email: %s" % (name, email)

        raise Exception("Lack client")

    def sendMessage(self, email, textMessage):
        for client in self.clients:
            if client["email"] == email:
                if type(textMessage) == str:
                    return "Send message to %s" % email
                else:
                    raise TypeError("Type text message have to be string")
        raise Exception("No client has this email")
    
    
from unittest.mock import *
from unittest import TestCase, main


class testSubscriber(TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_add_client_OK(self):
        self.temp.add = Mock()
        self.temp.add.return_value = [{"name": "Piotr", "email": "piotrnowak@example.com"}]

        result = self.temp.add("Piotr", "piotrnowak@example.com")
        self.assertListEqual(result, [{"name": "Piotr", "email": "piotrnowak@example.com"}])

    def test_add_client_BAD_exists(self):
        self.temp.add = Mock()
        self.temp.clients = [{"name": "Piotr", "email": "piotrnowak@example.com"}]
        self.temp.add.side_effect = Exception("This client exists")

        result = self.temp.add
        self.assertRaisesRegex(Exception, "This client exist", result, "Piotr", "piotrnowak@example.com")

    def test_add_client_BAD_name(self):
        self.temp.add = Mock()
        self.temp.add.side_effect = TypeError("Bad type name or/and email")
        result = self.temp.add
        self.assertRaisesRegex(TypeError, "Bad type name or/and email", result, 123, "piotrnowak@example.com")

    def test_delete(self):
        self.temp.delete = Mock()
        self.temp.clients = [{"name": "Wiktoria", "email": "wolnikowa@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.delete.return_value = "Delete: Wiktoria, email: wolnikowa@example.com"
        result = self.temp.delete("Wiktoria", "wolnikowa@example.com")
        self.assertEqual(result, "Delete: Wiktoria, email: wolnikowa@example.com")

    def test_delete_client_lack_client(self):
        self.temp.delete = Mock()
        self.temp.clients = [{"name": "Wiktoria", "email": "wolnikowa@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.delete.side_effect = Exception("Lack client")
        result = self.temp.delete
        self.assertRaisesRegex(Exception, "Lack client", result, "Filip", "filipostrowski@example.com")

    def test_send_message(self):
        self.temp.sendMessage = Mock()
        self.temp.clients = [{"name": "Wiktoria", "email": "wolnikowa@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.sendMessage.return_value = "Send message to kasiapolak@example.com"

        result = self.temp.sendMessage("kasiapolak@example.com", "Hello")
        self.assertEqual(result, "Send message to kasiapolak@example.com")

    def test_send_message_bad_type_message(self):
        self.temp.sendMessage = Mock()
        self.temp.clients = [{"name": "Wiktoria", "email": "wolnikowa@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.sendMessage.side_effect = TypeError("Type text message have to be string")

        result = self.temp.sendMessage
        self.assertRaisesRegex(TypeError, "Type text message have to be string", result, "kasiapolak@example.com",
                               False)

    def test_send_message_clients_BAD_email(self):
        self.temp.sendMessage = Mock()
        self.temp.clients = [{"name": "Wiktoria", "email": "wolnikowa@example.com"},
                             {"name": "Kasia", "email": "kasiapolak@example.com"}]
        self.temp.sendMessage.side_effect = Exception("No client has this email")

        result = self.temp.sendMessage
        self.assertRaisesRegex(Exception, "No client has this email", result, "bartekkowalslki@example.com", "Hello")


if __name__ == '__main__':
    main()