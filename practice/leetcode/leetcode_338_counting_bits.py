# Solution 1 - O(nlogn)

class Solution1:
    def count_bits(self, n: int) -> list[int]:
        res = []
        for num in range(n+1):
            count = 0
            while num!=0:
                count += num%2
                num //= 2
            res.append(count)
        return res