# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = [None]
        def dfs(root):
            if not root:
                return
            if root.val == val:
                res[0] = root
                return
            left = dfs(root.left)
            right = dfs(root.right)
            return
        dfs(root)
        return res[0]
