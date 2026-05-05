# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def nodeMaxDepth(treeNode):

            if not isinstance(treeNode, TreeNode):
                return 0

            if treeNode.left is not None:
                left_depth = 1 + nodeMaxDepth(treeNode.left)
            else:
                left_depth = 1
            if treeNode.right is not None:
                right_depth = 1 + nodeMaxDepth(treeNode.right)
            else:
                right_depth = 1

            return max(left_depth, right_depth)

        return nodeMaxDepth(root)


        # when node == 1
        # left = node2
        # right = node3
        # left_depth = 1 + node2_depth = 1 + 1 = 2
        # right_depth = 1 + node3_depth = 1 + max(node4_depth+1, 1) = 1 + max(1+1, 1) = 1 + max(2,1) = 3

            
        