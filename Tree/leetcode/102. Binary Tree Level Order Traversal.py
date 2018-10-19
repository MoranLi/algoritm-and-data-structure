class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
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
        return self.list