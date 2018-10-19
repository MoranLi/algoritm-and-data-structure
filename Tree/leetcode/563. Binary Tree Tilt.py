class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0

        def helper(root, sumx):
            if root:
                if root.left:
                    sumx += helper(root.left, 0)
                if root.right:
                    sumx += helper(root.right, 0)
                sumx += root.val
                return sumx
            else:
                return 0

        def helper2(root):
            if root:
                if not root.left and not root.right:
                    return 0
                else:
                    self.sum += abs(helper(root.left, 0) - helper(root.right, 0))
                    helper2(root.left)
                    helper2(root.right)

        helper2(root)
        return self.sum
        return abs(leftsum - rightsum)
