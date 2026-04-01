import math

class Base32Encoder:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

    @classmethod
    def encode(cls, data: bytes) -> str:
        if not data:
            return ""
            
        result = []
        buffer = 0
        bits_left = 0
        
        for byte in data:
            buffer = (buffer << 8) | byte
            bits_left += 8
            
            while bits_left >= 5:
                bits_left -= 5
                index = (buffer >> bits_left) & 0x1F
                result.append(cls.ALPHABET[index])
                
        if bits_left > 0:
            index = (buffer << (5 - bits_left)) & 0x1F
            result.append(cls.ALPHABET[index])
            
        padding = (8 - (len(result) % 8)) % 8
        result.extend(["="] * padding)
        
        return "".join(result)