# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depthesthelper(root,curr_depth,max_depth):
            if root:
                if not root.left and not root.right:
                    return curr_depth
                if root.left:
                    depthesthelper(root.left,curr_depth+1,max_depth),max_depth
                else:
                    return 0
                if root.right:
                    max_dpeth = max(depthesthelper(root.right,curr_depth+1,max_depth),max_depth)
                else:
                    return 0
                return max_depth
        max_left = 0
        max_right = 0
        if root.left:
            max_left = depthesthelper(root.left,1,max_left)
        if root.right:
            max_right = depthesthelper(root.right,1,max_right)
        return max_left+max_right