"""
Problem No. 23

You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use a mid heap ?
        heap = []
        heapify(heap)
        
        for node in lists:
            while node:
                heappush(heap, node.val)
                node = node.next
        
        dummy = curr = ListNode()
        while heap:
            val = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next