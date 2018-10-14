class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depthes = []

        def helper(root, depth, depthes):
            if root:
                if root.left:
                    helper(root.left, depth + 1, depthes)
                if root.right:
                    helper(root.right, depth + 1, depthes)
                else:
                    depthes.append(depth)

        if root:
            helper(root, 1, depthes)
        else:
            return 0
        return max(depthes)
