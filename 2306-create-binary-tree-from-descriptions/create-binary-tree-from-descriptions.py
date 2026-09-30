class Solution:
    def createBinaryTree(self, descriptions):
        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:

            # Create parent node if not already present
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)

            # Create child node if not already present
            if child not in nodes:
                nodes[child] = TreeNode(child)

            # Connect parent and child
            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            # Child cannot be the root
            children.add(child)

        # Find node that never appeared as a child
        for value in nodes:
            if value not in children:
                return nodes[value]