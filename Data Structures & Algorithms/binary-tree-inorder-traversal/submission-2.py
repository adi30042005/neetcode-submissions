# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs_inorder(root):
            if root is None:
                return
            
            dfs_inorder(root.left)
            result.append(root.val)
            dfs_inorder(root.right)

        dfs_inorder(root)
        return result