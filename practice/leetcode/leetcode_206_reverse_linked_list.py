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