# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p
        self.p_path = ""
        self.q_path = ""

        def dfs(root, path):
            if root:
                if root == p:
                    self.p_path = copy.deepcopy(path)
                if root == q:
                    self.q_path = copy.deepcopy(path)
                if root.left:
                    dfs(root.left, path + "l")
                if root.right:
                    dfs(root.right, path + "r")
                path = path[0:-1]

        dfs(root, "")
        print(self.p_path)
        print(self.q_path)
        pathx = ""
        for i in range(min(len(self.p_path), len(self.q_path))):
            if self.p_path[i] == self.q_path[i]:
                pathx += self.p_path[i]
            else:
                break
        p1 = root
        for i in pathx:
            if i == "l":
                p1 = p1.left
            else:
                p1 = p1.right
        return p1
