# Solution 1 - O(nlogn)


class Solution1:
    def count_bits(self, n: int) -> list[int]:
        res = []
        for num in range(n + 1):
            count = 0
            while num != 0:
                count += num % 2
                num //= 2
            res.append(count)
        return res


# Solution 2 - O(n)


class Solution2:
    def count_bits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
