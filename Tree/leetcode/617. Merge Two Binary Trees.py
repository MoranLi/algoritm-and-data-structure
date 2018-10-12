from TreeNode import TreeNode

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1!= None and t2 != None:
            t1.val = t1.val + t2.val
        elif t1 == None and t2 != None:
            t1 = TreeNode(t2.val)
        if t2 != None:
            if t2.left != None:
                t1.left = self.mergeTrees(t1.left,t2.left)
            if t2.right != None:
                t1.right = self.mergeTrees(t1.right,t2.right)
        return t1