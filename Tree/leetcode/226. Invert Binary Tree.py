class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(root):
            if root:
                subtreeleft = root.left
                root.left = root.right
                root.right = subtreeleft
                helper(root.left)
                helper(root.right)
        helper(root)
        return root