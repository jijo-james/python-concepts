# Solution 1

class Solution1:
    def hamming_weight(self, n: int) -> int:
        count = 0
        while n:
            count += n%2
            n = n >> 1
        return count 


# Solution 2

class Solution2:
    def hamming_weight(self, n: int) -> int:
        return bin(n).count('1')


# Solution 3

class Solution3:
    def hamming_weight(self, n:int) -> int:
        count = 0
        while n:
            n &= n-1
            count += 1
        return count 