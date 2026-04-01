class HyperLogLog:
    def __init__(self, p: int = 14):
        import math
        self.p = p
        self.m = 1 << p
        self.registers = [0] * self.m
        self.alpha_mm = (0.7213 / (1 + 1.079 / self.m)) * self.m * self.m
        
    def _hash(self, value: str) -> int:
        import hashlib
        h = hashlib.sha256(value.encode()).hexdigest()
        return int(h, 16)
        
    def _get_rho(self, w: int, max_width: int) -> int:
        rho = 1
        while rho <= max_width and not (w & 1):
            rho += 1
            w >>= 1
        return rho

    def add(self, value: str):
        x = self._hash(value)
        j = x & (self.m - 1)
        w = x >> self.p
        self.registers[j] = max(self.registers[j], self._get_rho(w, 256 - self.p))

    def count(self) -> float:
        import math
        Z = sum(math.pow(2, -r) for r in self.registers)
        E = self.alpha_mm / Z
        
        if E <= 2.5 * self.m:
            v = self.registers.count(0)
            if v > 0:
                return self.m * math.log(self.m / v)
        return E