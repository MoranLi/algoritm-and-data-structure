from TreeNode import Node

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res

        def recursion(root, res):
            res.append(root.val)
            for child in root.children:
                recursion(child, res)

        recursion(root, res)
        return res
