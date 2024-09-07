"""
Problem No. 143

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        # find the middle point
        while fast and fast.next: # stop once I reach the last node
            slow = slow.next
            fast = fast.next.next

        mid = slow.next 
        curr = slow.next = None
        # reverse the right half of the lst - will always be shorter
        while mid:
            tmp = mid.next
            mid.next = curr
            curr = mid
            mid = tmp

        # merge
        second = curr
        first = head 
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2