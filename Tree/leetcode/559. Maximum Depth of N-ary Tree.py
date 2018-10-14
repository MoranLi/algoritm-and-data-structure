from TreeNode import Node

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        depth = []
        def helper(node,count):
            if node.children:
                for i in node.children:
                    helper(i,count+1)
            depth.append(count)
        if root:
            helper(root,1)
        else:
            return 0
        return max(depth)