from TreeNode import TreeNode

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        def helper(root,depth,v,d):
            if depth == d-1:
                if root:
                    if root.left:
                        node = TreeNode(v)
                        temp = root.left
                        root.left = node
                        node.left = temp
                        if not root.right:
                            node2 = TreeNode(v)
                            root.right = node2
                            return
                    if root.right:
                        node = TreeNode(v)
                        temp = root.right
                        root.right = node
                        node.right = temp
                        if not root.left:
                            node2 = TreeNode(v)
                            root.left = node2
                            return
                    if not root.left and not root.right:
                        node = TreeNode(v)
                        node2 = TreeNode(v)
                        root.left = node
                        root.right = node2
                        return
            else:
                if root.left:
                    helper(root.left,depth+1,v,d)
                if root.right:
                    helper(root.right,depth+1,v,d)
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        else:
            helper(root,1,v,d)
            return root