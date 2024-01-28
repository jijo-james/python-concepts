class Solution:
    def three_sum(self, numbers: list[int]) -> list[int]:
        res = []
        numbers.sort()

        for i, n in enumerate(numbers):
            if i > 0 and n == numbers[i - 1]:
                continue

            left, right = 1, len(numbers) - 1
            while left < right:
                current_sum = n + numbers[left] + numbers[right]

                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    res.append([n, numbers[left], numbers[right]])
                    left += 1
                    while numbers[left] == numbers[left - 1] and left < right:
                        l += 1

        return res

s = Solution()
print(s.three_sum([-1,0,1,2,-1,-4]))