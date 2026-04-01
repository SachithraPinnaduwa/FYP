class SimpleSegmentTree:
    def __init__(self, arr: list):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) | 1]

    def update(self, idx: int, value: int):
        self.tree[idx + self.n] = value
        idx = idx + self.n
        while idx > 1:
            self.tree[idx >> 1] = self.tree[idx] + self.tree[idx ^ 1]
            idx >>= 1

    def query(self, left: int, right: int) -> int:
        res = 0
        left += self.n
        right += self.n
        while left < right:
            if left & 1:
                res += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                res += self.tree[right]
            left >>= 1
            right >>= 1
        return res