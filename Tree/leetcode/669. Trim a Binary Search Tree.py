from TreeNode import TreeNode

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        pre_root = TreeNode(R)
        pre_root.left = root
        def helper(pnode,node,L,R):
            if node.val < L:
                if node.right:
                    node = node.right
                    helper(pnode,node,L,R)
                else:
                    pnode.left = None
            elif node.val > R:
                if node.left:
                    node = node.left
                    helper(pnode,node,L,R)
                else:
                    pnode.right = None
            else:
                if node.val < pnode.val:
                    pnode.left = node
                else:
                    pnode.right = node
                if node.left:
                    helper(node,node.left,L,R)
                if node.right:
                    helper(node,node.right,L,R)
        helper(pre_root,root,L,R)
        return pre_root.left


solution = Solution()

a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)
e = TreeNode(2)
a.left = b
a.right = c
b.right = e

solution.trimBST(a,4,4)