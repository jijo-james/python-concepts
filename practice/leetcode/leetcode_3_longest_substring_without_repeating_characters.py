class Solution:
    def lengt_of_longest_substring(self, s: str) -> int:
        left = 0
        char_set = set()
        res = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            res = max(res, right - left + 1)

        return res
