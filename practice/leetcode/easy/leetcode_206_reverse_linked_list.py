# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative solution
class Solution1: 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        
        return previous
    
s1 = Solution1()
head = [1,2,3,4,5]
res1 = s1.reverseList(head)
print(res1)

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head