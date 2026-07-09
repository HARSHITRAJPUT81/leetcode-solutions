# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {value: i for i, value in enumerate(inorder)}
        preIndex = 0

        def build(left, right):
            nonlocal preIndex

            if left > right:
                return None

            rootVal = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootVal)

            mid = inorderIndex[rootVal]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)