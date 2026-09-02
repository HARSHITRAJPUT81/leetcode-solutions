class Solution:
    def deleteMiddle(self, head):
        # If only one node exists
        if head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete middle node
        prev.next = slow.next

        return head