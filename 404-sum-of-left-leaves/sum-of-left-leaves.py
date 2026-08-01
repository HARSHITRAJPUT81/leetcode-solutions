class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        ans = 0

        if root.left:
            # Check if left child is a leaf
            if root.left.left is None and root.left.right is None:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)

        ans += self.sumOfLeftLeaves(root.right)

        return ans