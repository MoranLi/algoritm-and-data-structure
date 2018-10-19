class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.list = []
        def helper(root,depth):
            if depth > len(self.list):
                self.list.append([])
            if root:
                if root.left:
                    helper(root.left,depth+1)
                if root.right:
                    helper(root.right,depth+1)
                self.list[depth-1].append(root.val)
        if root:
            helper(root,1)
        for i in range(0,len(self.list)):
            self.list[i] = self.list[i][-1]
        return self.list