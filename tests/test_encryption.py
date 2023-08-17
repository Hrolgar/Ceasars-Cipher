import unittest
from my_project.cipher_tool import encrypt, shift_cipher


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = "thisIsMyTestPassword1334?€&"
        self.shift = 11

    def test_inputExists(self):
        self.assertIsNotNone(self.my_message, "my_message is not defined")
        self.assertIsNotNone(self.shift, "shift is not defined")

    def test_inputType(self):
        self.assertIsInstance(self.my_message, str, "my_message is not a string")
        self.assertIsInstance(self.shift, int, "shift is not an integer")

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message, self.shift), str, "encrypt() does not return a string")

    def test_functReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message, self.shift), "encrypt() does not return anything")

    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message, self.shift)),
                         "encrypt() does not return a string of the same length as the input")

    def test_differentIO(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message, self.shift),
                         "encrypt() does not return a different string than the input")

    def test_shiftedCipher(self):
        encrypted_message = shift_cipher(self.my_message, self.shift)
        # print(encrypted_message)
        self.assertEqual(encrypted_message, encrypt(self.my_message, self.shift),
                         "encrypt() does not return a shifted cipher")


if __name__ == '__main__':
    unittest.main()
