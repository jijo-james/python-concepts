class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last = m + n - 1

        while n > 0 and m > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1


s = Solution()
s.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
