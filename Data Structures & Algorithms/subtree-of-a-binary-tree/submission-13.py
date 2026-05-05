# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        # loop over root tree and then search for the sub root value
        # if subroot value found then match all the elements of subroot with root

        self.subRootinRoot = None

        def matchSubRootinRoot(tree1, tree2):

            if type(tree1) != type(tree2):
                return False

            if tree1 is None and tree2 is None:
                return True
            
            if tree1.val != tree2.val:
                return False

            if type(tree1.left) != type(tree2.left):
                return False
            
            if type(tree1.right) != type(tree2.right):
                return False

            return True and matchSubRootinRoot(tree1.left, tree2.left) and matchSubRootinRoot(tree1.right, tree2.right)

        def findSubRootinRoot(root, subRoot):

            if not isinstance(root, TreeNode) or not isinstance(subRoot, TreeNode):
                return

            if root.val == subRoot.val and type(root.left) == type(subRoot.left) and type(root.right) == type(subRoot.right):
                self.subRootinRoot = root

            if self.subRootinRoot:
                if matchSubRootinRoot(self.subRootinRoot, subRoot):
                    return True


            if root.left is not None:
                output = findSubRootinRoot(root.left, subRoot)
                if output:
                    return True
            
            if root.right is not None:
                output = findSubRootinRoot(root.right, subRoot)
                if output:
                    return True

            return False

        
        return findSubRootinRoot(root, subRoot)
        