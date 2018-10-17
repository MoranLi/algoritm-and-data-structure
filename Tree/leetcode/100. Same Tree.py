class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def helper(rootp,rootq):
            if rootp and rootq:
                    return True and helper(rootp.left,rootq.left) and helper(rootp.right,rootq.right) and rootp.val == rootq.val
            elif not rootp and not rootq:
                return True
            else:
                return False
        return helper(p,q)