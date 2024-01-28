# Solution 1 - counting 1's by dividing with 2

class Solution1:
    def hamming_weight(self, n: int) -> int:
        count = 0
        while n:
            count += n%2
            n = n >> 1
        return count 


# Solution 2 - counting 1's using builtin bin function(binary)

class Solution2:
    def hamming_weight(self, n: int) -> int:
        return bin(n).count('1')


# Solution 3 - counting only 1's by eliminating one at a time, 
# using this method we don't have to iterate through every digit,
# it only iterating through 1's 

class Solution3:
    def hamming_weight(self, n:int) -> int:
        count = 0
        while n:
            n &= n-1
            count += 1
        return count 