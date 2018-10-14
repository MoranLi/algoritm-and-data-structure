class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = []
        def helper(root,depth,levels):
            if depth > len(levels):
                levels.append([])
            if root:
                if root.left:
                    helper(root.left,depth+1,levels)
                if root.right:
                    helper(root.right,depth+1,levels)
                levels[depth-1].append(root.val+0.0)
        if root:
            helper(root,1,levels)
        else:
            return 0
        results = []
        for i in range(0,len(levels)):
            sumx = sum(levels[i])
            results.append(sumx/len(levels[i]))
        return results