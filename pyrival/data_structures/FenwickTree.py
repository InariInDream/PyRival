class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * n

    @classmethod
    def from_array(cls, arr):
        tree = FenwickTree(len(arr))
        for i, v in enumerate(arr):
            tree.update(i, v)
        return tree

    def update(self, idx, delta):
        """Modifies the value at index idx by delta."""
        while idx < self.n:
            self.bit[idx] += delta
            idx |= (idx + 1)

    def query(self, idx):
        """Calculates the prefix sum for index idx."""
        return self.sum(idx - 1)

    def sum(self, right_idx):
        """Calculates the sum for the range [0, right_idx]."""
        res = 0
        while right_idx >= 0:
            res += self.bit[right_idx]
            right_idx = (right_idx & (right_idx + 1)) - 1
        return res

    def sum2(self, left_index, right_idx):
        """Calculates the sum for the range [left_idx, right_idx]."""
        return self.sum(right_idx) - self.sum(left_index - 1)

    def find_kth(self, k):
        """Finds the largest index idx such that its prefix sum <= k."""
        idx = -1
        for d in range(self.n.bit_length() - 1, -1, -1):
            right_idx = idx + (1 << d)
            if right_idx < self.n and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1