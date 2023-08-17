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
