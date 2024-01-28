class Solution:

    def max_product(self, nums: list[int]) -> int:
        
        result = max(nums)
        current_max, current_min = 1, 1

        for n in nums:
            temp = current_max
            current_max = max(current_max * n, current_min * n, n)
            current_min = min(temp * n, current_min * n, n)
            result = max(result, current_max)

        return result


s = Solution()
print(s.max_product([2,3,-2,4]))