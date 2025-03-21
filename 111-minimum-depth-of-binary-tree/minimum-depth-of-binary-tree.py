# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1
            

            left = dfs(root.left) if root.left else float('inf')
            right = dfs(root.right) if root.right else float('inf')
            return 1+min(left, right)
        return dfs(root)