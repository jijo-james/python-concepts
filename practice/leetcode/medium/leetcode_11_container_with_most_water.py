class Solution:
    def max_area(self, height: list[int]) -> int:
        res = 0

        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res


s = Solution()
print(s.max_area([1,8,6,2,5,4,8,3,7]))