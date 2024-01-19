# Solution 1: 

class Solution1:
    def missing_number(self, nums: list[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)

s1 = Solution1()
ans1 = s1.missing_number([9,6,4,2,3,5,7,0,1])

