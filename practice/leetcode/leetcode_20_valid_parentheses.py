class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in close_to_open:
                if stack and close_to_open[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return True if not stack else False
