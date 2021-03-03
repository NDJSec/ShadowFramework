from shadow.crypto.octal import *

def test_oct_decrypt():
    assert oct_decrypt('106 114 101 107') == 'FLAG'