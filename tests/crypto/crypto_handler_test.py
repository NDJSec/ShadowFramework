from click.testing import CliRunner
from shadow.crypto.crypto_handler import *
from shadow.__main__ import *

def test_crypto_handler_vignere_decrypt():
    runner = CliRunner()
    result = runner.invoke(crypto, ['--decrypt'], input='1\nGCYCZFMLYLEIM\nAYUSH\n')
    assert 'geeksforgeeks' in result.output 

def test_crypto_handler_caesar_decrypt(): 
    runner = CliRunner()
    result = runner.invoke(crypto, ['--decrypt'], input='2\nQjdpDUG{GMBH}\n0\npicoctf{\n')                                           
    assert 'picoctf{flag}' in result.output

def test_crypto_handler_binary_decrypt():
    runner = CliRunner()
    result = runner.invoke(crypto, ['--decrypt'], input='3\n01000110 01001100 01000001 01000111')  
    assert 'FLAG' in result.output
def test_crypto_handler_octal_decrypt():
    runner = CliRunner()
    result = runner.invoke(crypto, ['--decrypt'], input='4\n106 114 101 107')  
    assert 'FLAG' in result.output

def test_crypto_handler_hex_decrypt():
    runner = CliRunner()
    result = runner.invoke(crypto, ['--decrypt'], input='5\n46 4c 41 47')  
    assert 'FLAG' in result.output