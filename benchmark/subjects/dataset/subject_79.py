class MerkleNode:
    def __init__(self, left, right, hash_val: str):
        self.left = left
        self.right = right
        self.hash = hash_val

class MerkleTree:
    def __init__(self):
        self.root = None
        self.leaves = []

    def _hash(self, data: str) -> str:
        import hashlib
        return hashlib.sha256(data.encode()).hexdigest()

    def build(self, data_blocks: list):
        if not data_blocks:
            return
            
        self.leaves = [MerkleNode(None, None, self._hash(d)) for d in data_blocks]
        current_level = self.leaves
        
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                if i + 1 < len(current_level):
                    right = current_level[i + 1]
                    combined = left.hash + right.hash
                else:
                    right = left
                    combined = left.hash + left.hash
                    
                node = MerkleNode(left, right, self._hash(combined))
                next_level.append(node)
                
            current_level = next_level
            
        self.root = current_level[0] if current_level else None

    def get_root_hash(self) -> str:
        return self.root.hash if self.root else ""