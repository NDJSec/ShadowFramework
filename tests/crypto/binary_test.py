from shadow.crypto.binary import *

def test_binary_decrypt():
    assert binary_decrypt('01000110 01001100 01000001 01000111') == 'FLAG'