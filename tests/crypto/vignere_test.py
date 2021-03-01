import pytest
from shadow.crypto.vignere import *


def test_decrypt():
    assert decrypt('GCYCZFMLYLEIM', 'AYUSH') == 'geeksforgeeks'