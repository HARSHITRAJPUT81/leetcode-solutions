# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {value: i for i, value in enumerate(inorder)}
        postIndex = len(postorder) - 1

        def build(left, right):
            nonlocal postIndex

            if left > right:
                return None

            rootVal = postorder[postIndex]
            postIndex -= 1

            root = TreeNode(rootVal)
            mid = index[rootVal]

            # Build right subtree first
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
        