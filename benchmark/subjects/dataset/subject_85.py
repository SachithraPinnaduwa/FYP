class SkipList:
    def __init__(self, max_level: int, p: float):
        self.max_level = max_level
        self.p = p
        self.header = self._create_node(self.max_level, -1)
        self.level = 0
        import random
        self.random = random

    def _create_node(self, lvl, key):
        return {"key": key, "forward": [None] * (lvl + 1)}

    def _random_level(self):
        lvl = 0
        while self.random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, key: int):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current["forward"][i] and current["forward"][i]["key"] < key:
                current = current["forward"][i]
            update[i] = current

        current = current["forward"][0]

        if current is None or current["key"] != key:
            rlevel = self._random_level()

            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel

            n = self._create_node(rlevel, key)
            for i in range(rlevel + 1):
                n["forward"][i] = update[i]["forward"][i]
                update[i]["forward"][i] = n