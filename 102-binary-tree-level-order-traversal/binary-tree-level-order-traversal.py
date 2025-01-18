# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        myQueue = collections.deque()
        myQueue.append(root)
        while len(myQueue) > 0 and root:
            qLen = len(myQueue)
            level = []
            for i in range(qLen):
                node = myQueue.popleft()
                print("call", end="-")
                if node:
                    level.append(node.val)
                    myQueue.append(node.left)
                    myQueue.append(node.right)
            print("\n")
            if level:
                result.append(level)
        return result