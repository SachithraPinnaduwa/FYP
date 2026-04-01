import hashlib
import time

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        h = hashlib.sha256()
        h_str = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}".encode()
        h.update(h_str)
        return h.hexdigest()

class SimpleBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: str):
        prev_block = self.get_latest_block()
        new_block = Block(prev_block.index + 1, prev_block.hash, time.time(), data)
        self.chain.append(new_block)

    def is_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]
            
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != prev.hash:
                return False
        return True