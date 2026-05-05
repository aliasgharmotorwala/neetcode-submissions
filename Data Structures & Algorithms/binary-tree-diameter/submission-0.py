# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diameter = 0

        def maxNodeDepth(treeNode):

            if not isinstance(treeNode, TreeNode):
                return 0
            if treeNode.left is not None:
                left_depth = 1 + maxNodeDepth(treeNode.left)
            else:
                left_depth = 0
            if treeNode.right is not None:
                right_depth = 1 + maxNodeDepth(treeNode.right)
            else:
                right_depth = 0

            max_depth = max(left_depth, right_depth)

            node_diameter = left_depth + right_depth

            if node_diameter > self.max_diameter:
                self.max_diameter = node_diameter
            
            return max_depth

        maxNodeDepth(root)

        return self.max_diameter
        