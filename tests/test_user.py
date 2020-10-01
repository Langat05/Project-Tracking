import unittest

from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='student', email = "test@test.com",password='qwerty')

    def test_password_setter(self):
        self.assertTrue(self.new_user.hashed_password) 

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.hashed_password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('qwerty'))

    def test_password_reset_token(self):
        with self.assertRaises(AttributeError):
            self.new_user.hashed_password
