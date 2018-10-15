class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root,depth,listx):
            if depth > len(listx):
                listx.append([])
            if root:
                if root.left:
                    helper(root.left,depth+1,listx)
                if root.right:
                    helper(root.right,depth+1,listx)
                listx[depth-1].append(root.val)
        listx = []
        if root:
            helper(root,1,listx)
        else:
            return []
        results = []
        for i in listx:
            results.append(max(i))
        return results