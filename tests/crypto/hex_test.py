from shadow.crypto.hexadecimal import *

def test_hex_decrypt():
    assert hex_decrypt('46 4c 41 47') == 'FLAG'
