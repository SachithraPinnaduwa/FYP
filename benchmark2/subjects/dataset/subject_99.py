class VigenereCipher:
    def __init__(self, key: str):
        self.key = key.upper()

    def encrypt(self, plain_text: str) -> str:
        result = []
        key_idx = 0
        for char in plain_text.upper():
            if char.isalpha():
                p = ord(char) - 65
                k = ord(self.key[key_idx % len(self.key)]) - 65
                c = (p + k) % 26
                result.append(chr(c + 65))
                key_idx += 1
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, cipher_text: str) -> str:
        result = []
        key_idx = 0
        for char in cipher_text.upper():
            if char.isalpha():
                c = ord(char) - 65
                k = ord(self.key[key_idx % len(self.key)]) - 65
                p = (c - k + 26) % 26
                result.append(chr(p + 65))
                key_idx += 1
            else:
                result.append(char)
        return "".join(result)