#Solution 1

class Solution():

    def contains_duplicates(self, nums: list[int]) -> bool:

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

s1 = Solution()
# print(s1.contains_duplicates([1,2,3,1]))



# Solution 2

class Solution2:

    def contains_duplicate(self, nums: list[int]) -> bool:
        nums.sort()
        list_length = len(nums) - 1
        for i in range(list_length):
            if nums[i] == nums[i+1]:
                return True 
        return False


s2 = Solution2()

print(s2.contains_duplicate([1,2,3,1]))
