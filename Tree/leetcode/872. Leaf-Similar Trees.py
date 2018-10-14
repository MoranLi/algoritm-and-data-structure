from TreeNode import TreeNode

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leafOne = []
        leafTwo = []
        def helper(root,listx):
            if root:
                if root.left == None and root.right == None:
                    listx.append(root.val)
                    return
                helper(root.left,listx)
                helper(root.right,listx)
        helper(root1,leafOne)
        helper(root2,leafTwo)
        return leafOne == leafTwo