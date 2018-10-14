from TreeNode import TreeNode

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        preroot = TreeNode(0)
        p1 = preroot
        def helper(root,p1):
            if root:
                if root.left:
                    helper(root.left,p1)
                node = TreeNode(root.val)
                p1.right = node
                p1 = node
                if root.right:
                    helper(root.right,p1)
        helper(root,p1)
        return preroot.right

a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(4)
e = TreeNode(1)
a.left = b
a.right = c
b.left = e

solution = Solution()

solution.increasingBST(a)