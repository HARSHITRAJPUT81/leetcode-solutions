# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.head = head

        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            leftChild = build(left, mid - 1)

            root = TreeNode(self.head.val)
            root.left = leftChild

            self.head = self.head.next

            root.right = build(mid + 1, right)

            return root

        n = getLength(head)
        return build(0, n - 1)