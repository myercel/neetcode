"""
Problem No. 206

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev 
        
        """
        # Recursive option
        if not head:
            return None
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newhead
        """
        """
        My solution: uses extra mem space
        tmp = curr = None

        while head:
            curr = ListNode(head.val)
            curr.next = tmp
            tmp = curr
            head = head.next

        return curr
        """