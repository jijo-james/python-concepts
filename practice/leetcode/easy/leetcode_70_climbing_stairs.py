class Solution:
    def climb_stairs(self, n: int) -> int:
        left, right = 1, 1

        for i in range(n - 1):
            left, right = right + left, left
        return left