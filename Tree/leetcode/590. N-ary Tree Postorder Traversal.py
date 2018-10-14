from TreeNode import Node

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        results = []
        def helper(node):
            if node.children != []:
                for i in node.children:
                    helper(i)
            results.append(node.val)
        if root:
            helper(root)
        return results