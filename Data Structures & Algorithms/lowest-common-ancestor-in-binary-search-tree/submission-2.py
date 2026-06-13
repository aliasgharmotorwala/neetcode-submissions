# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        self.lca_node = None
        self.nodes = {}

        def parseTree(node: TreeNode) -> bool:

            if node in self.nodes:
                return self.nodes[node]
            
            if node is None:
                return False

            if node.val in [p.val, q.val]:
                if parseTree(node.left) or parseTree(node.right):
                    self.lca_node = node
                self.nodes.update({node: True})
                return self.nodes[node]

            if parseTree(node.left) and parseTree(node.right):
                self.lca_node = node
                self.nodes.update({node: True})
                return self.nodes[node]

            if parseTree(node.left) or parseTree(node.right):
                self.nodes.update({node: True})
            else:
                self.nodes.update({node: False})
            return self.nodes[node]

        parseTree(root)
        return self.lca_node