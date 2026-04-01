class ABTestAssigner:
    def __init__(self, salt: str = "salt_v1"):
        self.salt = salt
        self.experiments = {}

    def add_experiment(self, exp_name: str, variants: dict):
        # variants = {"A": 50, "B": 50}
        total = sum(variants.values())
        if total != 100:
            raise ValueError("Variants must sum to 100")
            
        ranges = []
        current = 0
        for name, pct in variants.items():
            ranges.append((name, current, current + pct))
            current += pct
            
        self.experiments[exp_name] = ranges

    def get_variant(self, user_id: str, exp_name: str) -> str:
        if exp_name not in self.experiments:
            return "Control"
            
        import hashlib
        key = f"{user_id}_{exp_name}_{self.salt}"
        h = int(hashlib.md5(key.encode()).hexdigest()[:8], 16)
        val = h % 100
        
        for name, start, end in self.experiments[exp_name]:
            if start <= val < end:
                return name
        return "Control"