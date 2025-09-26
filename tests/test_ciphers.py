import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ciphers import caesar_encrypt, caesar_decrypt, vigenere_encrypt, vigenere_decrypt
from ciphers import caesar_encrypt, caesar_decrypt, vigenere_encrypt, vigenere_decrypt

def test_caesar_basic():
    pt = "Hello, World!"
    ct = caesar_encrypt(pt, 5)
    assert caesar_decrypt(ct, 5) == pt

def test_vigenere_basic():
    pt = "Attack at Dawn!"
    key = "LEMON"
    ct = vigenere_encrypt(pt, key)
    assert vigenere_decrypt(ct, key) == pt

