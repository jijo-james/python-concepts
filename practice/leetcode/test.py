class Solution:

    def two_sum(self, array: list[int], target: int) -> list[int]:
        
        previous_map = {}
        for i,n in enumerate(array):
            difference = target - n
            if difference in previous_map:
                return [i, previous_map[difference]]
            previous_map[n] = i

        return
s = Solution()

print(s.two_sum([1,2,3,4,5,6,7], 10))
