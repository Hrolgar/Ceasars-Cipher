import unittest
import string

ABC = string.ascii_letters + "øæåØÆÅ" + string.punctuation + string.digits + " "


def calc_shift(_idx: int, input_shift: int) -> int:
    if len(ABC) > (_idx + input_shift):
        return _idx + input_shift
    else:
        return input_shift - (len(ABC) - _idx)


def shift_cipher(input_message: str, input_shift: int) -> str:
    input_shift = 1 if input_shift <= 0 else input_shift
    _encrypted_message = "".join([ABC[calc_shift(ABC.find(char), input_shift)] for index, char in enumerate(input_message)])
    return _encrypted_message


def encrypt(input_message: str, input_shift: int) -> str:
    _encrypted_message = shift_cipher(input_message, input_shift)
    return _encrypted_message


def get_input() -> tuple:
    input_message = input("Please enter message to encrypt: ")
    while not input_message or input_message.isspace() or len(input_message) < 6:
        print("Message cannot be empty or less than 6 characters")
        input_message = input("Please enter message to encrypt: ")

    input_shift = int(input("Enter shift: "))
    while not input_shift:
        print("Shift cannot be empty")
        input_shift = int(input("Enter shift: "))
    return input_message, input_shift


while True:
    print("Welcome to my Ceasar's Cipher encryption tool, with Python Unit Testing!")
    message, shift = get_input()
    print(f"You entered: {message} with shift: {shift}")
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    break


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
