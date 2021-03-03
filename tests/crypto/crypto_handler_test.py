from shadow.crypto.crypto_handler import *

def test_crypto_handler_vignere_decrypt():
    crypto_handler.crypto.vignere_cipher = 'GCYCZFMLYLEIM'
    crypto_handler.crypto.key = 'AYUSH'
    assert crypto_handler.crypto(None, 'decrypt', '1') == 'geeksforgeeks'   

def test_crypto_handler_caesar_decrypt():                                            
    # crypto_handler.crypto.caesar_cipher = 'QjdpDUG{GMBH}'
    # crypto_handler.crypto.shift = 0
    # crypto_handler.crypto.flag_start = 'picoctf{'
    # assert crypto_handler.crypto(None, 'decrypt', '2') == 'picoctf{flag}'
    pass

def test_crypto_handler_binary_decrypt(monkeypatch):
    monkeypatch.setattr('binary_input', lambda: '01000110 01001100 01000001 01000111') 
    assert crypto_handler.crypto(None, 'decrypt', '3') == 'FLAG' 

def test_crypto_handler_vignere_decrypt():
    pass

def test_crypto_handler_vignere_decrypt():
    pass