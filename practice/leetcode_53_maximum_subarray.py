class Solution:

    def max_subarray(self, numbers: list[int]) -> int :
        max_subarray = numbers[0]
        current_sum = 0

        for n in numbers:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_subarray = max(max_subarray, current_sum)
