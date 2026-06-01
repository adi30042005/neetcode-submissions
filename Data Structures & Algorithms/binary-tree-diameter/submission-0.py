# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is longest path of a node's left and right added
        # the longest path between 2 nodes is the number of edges
        # post order traversal since we will be accessing children first
        dia = 0

        def dfs(root):
            nonlocal dia

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            dia = max(dia, left + right)

            return 1 + max(left,right)
        
        dfs(root)
        return dia
        


        