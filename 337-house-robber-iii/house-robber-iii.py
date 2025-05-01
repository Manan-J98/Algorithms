# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]  # [rob, skip]

            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1]  # can't rob children
            skip = max(left) + max(right)        # can rob or skip children

            return [rob, skip]
        res = dfs(root)
        return max(res)