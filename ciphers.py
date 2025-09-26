def caesar_encrypt(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)
def vigenere_encrypt(text: str, key: str) -> str:
    key_shifts = [ord(k.lower()) - 97 for k in key if k.isalpha()]
    if not key_shifts:
        raise ValueError("Key must contain letters")
    res = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = key_shifts[ki % len(key_shifts)]
            res.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            res.append(ch)
    return ''.join(res)

def vigenere_decrypt(text: str, key: str) -> str:
    key_shifts = [ord(k.lower()) - 97 for k in key if k.isalpha()]
    if not key_shifts:
        raise ValueError("Key must contain letters")
    res = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = key_shifts[ki % len(key_shifts)]
            res.append(chr((ord(ch) - base - shift) % 26 + base))
            ki += 1
        else:
            res.append(ch)
    return ''.join(res)

