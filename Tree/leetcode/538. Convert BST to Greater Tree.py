class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(root,res):
            if root:
                if root.right:
                    res = helper(root.right,res)
                root.val+=res
                res = root.val
                if root.left:
                    res = helper(root.left,res)
                return res
        helper(root,0)
        return root