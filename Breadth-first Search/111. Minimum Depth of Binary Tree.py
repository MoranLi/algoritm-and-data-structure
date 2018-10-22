# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root,depth):
            if root:
                if root.left == None and root.right == None:
                    return depth
                return min(helper(root.right,depth+1),helper(root.left,depth+1))
            else:
                return 2**31-1
        return helper(root,1) if root else 0