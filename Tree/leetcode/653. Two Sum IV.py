class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def helper(root,listx):
            if root:
                listx.append(root.val)
                if root.left:
                    helper(root.left,listx)
                if root.right:
                    helper(root.right,listx)
        listx = []
        helper(root,listx)
        y = {}
        for i in listx:
            com = k - i
            try:
                if com in y:
                    return True
            except KeyError:
                pass
            y[i] = i
        return False