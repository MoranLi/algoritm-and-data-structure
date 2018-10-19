class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if root != None:
                if root.left == None and root.right == None:
                    return [0,root.val]
                left = helper(root.left)
                right = helper(root.right)
                return [max(left[0],left[1])+max(right[0],right[1]),root.val+left[0]+right[0]]
            else:
                return [0,0]
        result = helper(root)
        return max(result[0],result[1])