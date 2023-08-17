import cipher_tool as ct
import database as db


def input_with_validation(prompt: str, validation: callable, error_message: str) -> str:
    value = input(prompt)
    while not validation(value):
        print(error_message)
        value = input(prompt)
    return value


def get_input() -> tuple:
    input_app_name = input_with_validation("Please enter the name of the application the password is linked to: ",
                                           lambda x: x and not x.isspace() and len(x) >= 3,
                                           "Application name cannot be empty or less than 3 characters")

    input_message = input_with_validation("Please enter the password you want to encrypt: ",
                                          lambda x: x and not x.isspace() and len(x) >= 3,
                                          "Password cannot be empty or less than 3 characters")

    input_shift = input_with_validation("Please enter the shift you want to use for encryption: ",
                                        lambda x: x and not x.isspace() and x.isdigit(),
                                        "Shift cannot be empty or less than 1 character")

    return input_app_name, input_message, int(input_shift)


if __name__ == '__main__':
    while True:
        print("Welcome to my Ceasar's Cipher encryption tool, with Python Unit Testing!")
        app_name, message, shift = get_input()
        print(f"You entered: {message} with shift: {shift}")
        encrypted_message = ct.encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
        break
