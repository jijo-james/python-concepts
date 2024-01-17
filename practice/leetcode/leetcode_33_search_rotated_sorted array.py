class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)-1
        
        while low <= high:
            mid = (low+high)//2
            if target == nums[mid]:
                return mid

            if nums[low]<=nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid+1
                else:
                    high = mid - 1
            
            else:
                if target < num[mid] or target > num[high]:
                    high = mid -1
                else:
                    low = mid+1

        return -1
