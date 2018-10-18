# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root,sumx):
            if root:
                if root.left:
                    if root.left.left == None and root.left.right == None:
                        sumx+=root.left.val
                    else:
                        sumx = helper(root.left,sumx)
                if root.right:
                    sumx = helper(root.right,sumx)
                return sumx
        sumx = 0
        if root:
            sumx = helper(root,sumx)
        else:
            return 0
        return sumx

solution = Solution()

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
d.right = e

solution.sumOfLeftLeaves(a)