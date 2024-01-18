# Solution 1

class Solution1:
    def hamming_weight(self, n: int) -> int:
        count = 0
        while n:
            count += n%2
            n = n >> 1
        return count 

# Solution 2

class Solution1:
    def hamming_weight(self, n: int) -> int:
        return bin(n).count('1')