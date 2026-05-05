# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isBalanced = True

        def nodeDepth(treeNode):
            
            if not isinstance(treeNode, TreeNode):
                return 0

            if treeNode.left is not None:
                left_depth = 1 + nodeDepth(treeNode.left)
            else:
                left_depth = 0

            if treeNode.right is not None:
                right_depth = 1 + nodeDepth(treeNode.right)
            else:
                right_depth = 0

            if abs(left_depth-right_depth) > 1:
                self.isBalanced = False

            return max(left_depth, right_depth)

        nodeDepth(root)

        return self.isBalanced
            
