class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = []

        def helper(root, depth, last, nodes):
            if root:
                if root.left:
                    helper(root.left, depth + 1, "L", nodes)
                if root.right:
                    helper(root.right, depth + 1, "R", nodes)
                else:
                    nodes.append([depth, root.val])

        helper(root, 1, "L", nodes)
        max_depth = 0
        max_value = 0
        for i in nodes:
            if i[0] > max_depth:
                max_depth = i[0]
                max_value = i[1]
        return max_value
