class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(root,listx):
            if root.left:
                helper(root.left,listx)
            listx.append(root.val)
            if root.right:
                helper(root.right,listx)
        listx = []
        helper(root,listx)
        return listx[k-1]