# Ceasar's Cipher Encryption Tool

This Python application allows you to apply a Caesar's Cipher (a type of substitution cipher) on your input text. It also includes a suite of unit tests.

## Features

1. Input validation for application name, message, and shift value.
2. Encryption using a Caesar's Cipher method.
3. Unit tests to ensure the program works as expected.

## How To Use

1. Run `main.py`.
2. When prompted, enter the name of the application.
3. Enter the password you wish to encrypt.
4. Enter the shift you want to use for encryption. This is the number of positions each letter in the password will be shifted. 

## Unit Tests

The unit tests are located in `test_encryption.py`. 

To run the tests, use the command: `python -m unittest -v test_encryption.py`

These tests include checks for:

- Input and output types.
- Existence of input and output.
- Length and content of the output string.

## Authors

- [@Hrolgar](https://github.com/Hrolgar)

## Disclaimer

This tool is meant for educational purposes only. It's not recommended to use this tool for encrypting sensitive data or for any malicious purposes.

Always use strong, unique passwords and store them securely.