class Solution():

    def contains_duplicates(self, nums: list[int]) -> bool:

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

s = Solution()
print(s.contains_duplicates([1,2,3,1]))