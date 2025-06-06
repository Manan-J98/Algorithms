# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        index = [0]

        def dfs():
            if vals[index[0]] == "#":
                index[0] += 1
                return None
            node = TreeNode(int(vals[index[0]]))
            index[0] += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))