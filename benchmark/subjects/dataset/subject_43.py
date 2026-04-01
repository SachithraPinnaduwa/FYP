class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift % 26

    def _shift_char(self, char: str, shift: int) -> str:
        if not char.isalpha():
            return char
        offset = 65 if char.isupper() else 97
        return chr((ord(char) - offset + shift) % 26 + offset)

    def encrypt(self, text: str) -> str:
        return "".join(self._shift_char(c, self.shift) for c in text)

    def decrypt(self, text: str) -> str:
        return "".join(self._shift_char(c, -self.shift) for c in text)