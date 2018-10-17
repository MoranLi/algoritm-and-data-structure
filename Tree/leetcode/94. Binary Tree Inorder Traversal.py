class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(root, listx):
            if root:
                if root.left:
                    helper(root.left, listx)
                listx.append(root.val)
                if root.right:
                    helper(root.right, listx)

        listx = []
        helper(root, listx)
        return listx
