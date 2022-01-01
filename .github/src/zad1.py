import requests


class RandomUser:
    def __init__(self):
        self.url = 'https://randomuser.me/api/'

    def get_user(self):
        res = requests.get(self.url)

        return res.json()["results"][0]

    def get_user_with_gender(self, gender):
        if type(gender) != str:
            raise TypeError("gender must be of a string type")
        elif gender != "male" and gender != "female":
            raise ValueError("gender must be either male or female")

        res = requests.get(f'{self.url}?gender={gender}')

        return res.json()["results"][0]

    def get_user_with_nationality(self, nationality):
        possible_nationalities = ['AU', 'BR', 'CA', 'CH', 'DE', 'DK', 'ES', 'FI', 'FR', 'GB', 'IE', 'IR', 'NO', 'NL',
                                  'NZ', 'TR', 'US']
        if type(nationality) != str:
            raise TypeError("nationality must be of a string type")
        elif nationality not in possible_nationalities:
            raise ValueError("nationality was not recognized")

        res = requests.get(f'{self.url}?nat={nationality}')

        return res.json()["results"][0]

import unittest


class TestRandomUser(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_random_user_get_user_returns_dict(self):
        user = self.temp.get_user()
        self.assertIsInstance(user, dict)

    def test_random_user_get_user_has_name(self):
        user = self.temp.get_user()
        self.assertIsInstance(user["name"]["first"], str)

    def test_random_user_get_user_with_gender_returns_dict(self):
        user = self.temp.get_user_with_gender("male")
        self.assertIsInstance(user, dict)

    def test_random_user_get_user_with_gender_male_returns_male_user(self):
        user = self.temp.get_user_with_gender("male")
        self.assertEqual(user["gender"], "male")

    def test_random_user_get_user_with_gender_integer_raises_typeError(self):
        self.assertRaises(TypeError, self.temp.get_user_with_gender, 123)

    def test_random_user_get_user_with_gender_incorrect_raises_valueError(self):
        self.assertRaises(ValueError, self.temp.get_user_with_gender, "andrzej")

    def test_random_user_get_user_with_nationality(self):
        user = self.temp.get_user_with_nationality("AU")
        self.assertIsInstance(user, dict)

    def test_random_user_get_user_with_nationality_returns_correct_nationality(self):
        user = self.temp.get_user_with_nationality("AU")
        self.assertEqual(user["location"]["country"], "Australia")

    def test_random_user_get_user_with_nationality_integer_raises_typeError(self):
        self.assertRaises(TypeError, self.temp.get_user_with_nationality, 123)

    def test_random_user_get_user_with_nationality_incorrect_raises_valueError(self):
        self.assertRaises(ValueError, self.temp.get_user_with_nationality, "PL")

    def tearDown(self):
        self.temp = None


import unittest
from unittest.mock import Mock, patch
from unittest.mock import *
from src.zad1MockResults.py import *
class TestRandomUser(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_random_user_get_user(self):
        self.temp.get_user = MagicMock(return_value=random_user_result)
        self.assertEqual(self.temp.get_user(), random_user_result)

    def test_random_user_get_user_with_gender(self):
        self.temp.get_user_with_gender = MagicMock(return_value=random_user_with_gender_result)
        self.assertEqual(self.temp.get_user_with_gender(), random_user_with_gender_result)

    def test_random_user_get_user_with_nationality(self):
        self.temp.get_user_with_nationality = MagicMock(return_value=random_user_with_nationality_result)
        self.assertEqual(self.temp.get_user_with_nationality(), random_user_with_nationality_result)

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()