"""
Problem No. 19

Given the head of a linked list, remove the nth node from the 
end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        left = dummy
        right = head

        # position right pointer properly
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # nposition left pointer at the node before n
        while right: # stop at the last node
            right = right.next
            left = left.next

        # left.next = nth node
        left.next = left.next.next

        return dummy.next