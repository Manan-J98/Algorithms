# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # main intuition - dynamic programming, need path sum of left and right subtrees for each node
    # base condition - if not root
    # hypothesis - we get the res from left and right subtrees
    # induction - either return the max of left, right subtress + the curVal
    # left and right subtress could return val less than or -ve than curVal, so can return just curVal  
    # return max of two
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]

        def dfs(root):
            if not root:
                return 0

            # hypothesis    
            left = dfs(root.left)
            right = dfs(root.right)

            # induction
            temp = max(max(left, right) + root.val,root.val)
            ans = max(temp, left + right + root.val)
            res[0] = max(res[0], ans)
            return temp
        dfs(root)
        return res[0]


        