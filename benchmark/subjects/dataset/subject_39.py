class Base58Encoder:
    ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    @classmethod
    def encode(cls, b: bytes) -> str:
        n = int.from_bytes(b, "big")
        result = []
        while n > 0:
            n, rem = divmod(n, 58)
            result.append(cls.ALPHABET[rem])
            
        for byte in b:
            if byte == 0:
                result.append(cls.ALPHABET[0])
            else:
                break
                
        return "".join(reversed(result))

    @classmethod
    def decode(cls, s: str) -> bytes:
        n = 0
        for char in s:
            n = n * 58 + cls.ALPHABET.index(char)
            
        h = n.to_bytes((n.bit_length() + 7) // 8, "big")
        
        pad = 0
        for char in s:
            if char == cls.ALPHABET[0]:
                pad += 1
            else:
                break
                
        return (b'\0' * pad) + h