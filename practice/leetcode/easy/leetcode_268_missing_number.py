# Solution 1:


class Solution1:
    def missing_number(self, nums: list[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


s1 = Solution1()
ans1 = s1.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])


# Solutuion 2 - xor the two lists


class Solution2:
    def missing_number(self, nums: list[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res


s2 = Solution2()
ans2 = s2.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])
