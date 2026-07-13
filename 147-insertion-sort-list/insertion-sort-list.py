# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head

        while curr:
            prev = dummy

            # Find the correct position to insert curr
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            next_node = curr.next

            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            curr = next_node

        return dummy.next