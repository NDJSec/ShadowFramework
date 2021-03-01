import pytest
from shadow.crypto.caesar import *


def test_decrypt():
    assert decrypt('QjdpDUG{GMBH}', 1) == 'picoctf{flag}'
    assert decrypt('WpjvJAM{MSHN}', 7) == 'picoctf{flag}'

def test_guess():
    assert guess('QjdpDUG{GMBH}', 'picoctf{') == 'picoctf{flag}'
    assert guess('QjdpDUG{GMBH}', 'PicoCTF{') == 'picoctf{flag}'
