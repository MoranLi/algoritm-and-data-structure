# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import os


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        code = ''
        listx = []

        def helper(root, depth, code, listx):
            if root:
                if root.left:
                    helper(root.left, depth, code + 'l', listx)
                if root.right:
                    helper(root.right, depth, code + 'r', listx)
                listx.append(code)

        helper(root, 0, code, listx)
        max_depth = 0
        for i in listx:
            if len(i) > max_depth:
                max_depth = len(i)
        listz = []
        for i in listx:
            if len(i) == max_depth:
                listz.append(i)
        path = os.path.commonprefix(listz)
        node = root
        for i in path:
            if i == 'l':
                node = node.left
            else:
                node = node.right
        return node
