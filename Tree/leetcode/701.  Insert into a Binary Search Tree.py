from TreeNode import TreeNode

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        node = root
        pnode = root
        if val < root.val:
            node = node.left
        elif val > root.val:
            node = node .right
        while node != None:
            pnode = node
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node .right
        if val < pnode.val:
            pnode.left = TreeNode(val)
        else:
            pnode.right = TreeNode(val)
        return root