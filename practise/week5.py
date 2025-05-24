class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right):
        left += self.n
        right += self.n
        max_value = 0
        while left < right:
            if left % 2:
                max_value = max(max_value, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                max_value = max(max_value, self.tree[right])
            left //= 2
            right //= 2
        return max_value

def find_total_xp(N, A, Bonus):
    # Step 1: Build the Segment Tree for Bonus
    seg_tree = SegmentTree(Bonus)

    total_xp = 0

    # Step 2: Find the first player R on the right for each player i
    for i in range(N):
        power_i = A[i]
        R = -1
        for j in range(i + 1, N):
            if A[j] % power_i == 0:
                R = j
                break
        if R != -1:
            # Step 3: Query the maximum bonus in the range [i, R]
            max_bonus = seg_tree.query(i, R + 1)
            total_xp += max_bonus

    return total_xp

# Example usage:
N = 4
A = [1, 1, 2, 2]
Bonus = [4, 8, 2, 1]

print(find_total_xp(N, A, Bonus))  # Output: 18

