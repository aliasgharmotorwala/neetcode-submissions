# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        self.isSameTree = True

        def areNodesSame(p, q):

            if isinstance(p, TreeNode) != isinstance(q, TreeNode):
                self.isSameTree = False
                return 
            
            if p is None and q is None:
                return

            if p.val != q.val:
                self.isSameTree = False
            
            areNodesSame(p.left, q.left)

            areNodesSame(p.right, q.right)

        areNodesSame(p, q)

        return self.isSameTree
            


        