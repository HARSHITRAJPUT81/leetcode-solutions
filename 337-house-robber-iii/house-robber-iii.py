# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)   # (not_rob, rob)

            left_not, left_rob = dfs(node.left)
            right_not, right_rob = dfs(node.right)

            rob = node.val + left_not + right_not
            not_rob = max(left_not, left_rob) + max(right_not, right_rob)

            return (not_rob, rob)

        return max(dfs(root))