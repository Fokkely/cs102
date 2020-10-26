def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    k = 0
    for i in plaintext:
        shift = ord(keyword[k % len(keyword)].lower()) - 97
        k += 1
        if ord("a") <= ord(i) <= ord("z"):
            if ord(i) + shift > ord("z"):
                ciphertext += chr(ord(i) + shift - 26)
            else:
                ciphertext += chr(ord(i) + shift)
        elif ord("A") <= ord(i) <= ord("Z"):
            if ord(i) + shift > ord("Z"):
                ciphertext += chr(ord(i) + shift - 26)
            else:
                ciphertext += chr(ord(i) + shift)
        else:
            ciphertext += i
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    k = 0
    for i in ciphertext:
        shift = ord(keyword[k % len(keyword)].lower()) - 97
        k += 1
        if ord("a") <= ord(i) <= ord("z"):
            if ord(i) - shift < ord("a"):
                plaintext += chr(ord(i) - shift + 26)
            else:
                plaintext += chr(ord(i) - shift)
        elif ord("A") <= ord(i) <= ord("Z"):
            if ord(i) - shift < ord("A"):
                plaintext += chr(ord(i) - shift + 26)
            else:
                plaintext += chr(ord(i) - shift)
        else:
            plaintext += i
    return plaintext
