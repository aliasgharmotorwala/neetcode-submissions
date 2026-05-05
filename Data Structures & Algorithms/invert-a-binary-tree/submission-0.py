# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invertTree(treeNode):
            if not isinstance(treeNode, TreeNode):
                return None
            left = treeNode.left
            right = treeNode.right
            treeNode.left = right
            treeNode.right = left
            if right is not None:
                invertTree(right)
            if left is not None:
                invertTree(left)

        invertTree(root)

        return root

        