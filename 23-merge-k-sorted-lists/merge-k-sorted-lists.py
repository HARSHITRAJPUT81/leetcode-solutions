from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Put first node of each list into heap
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            value, i, node = heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next
        