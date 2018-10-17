class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root,listz):
            if root:
                listz.append(root.val)
                if root.left:
                    helper(root.left,listz)
                if root.right:
                    helper(root.right,listz)
        listz = []
        if root:
            helper(root,listz)
        return listz