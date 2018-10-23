# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy


class Solution(object):
    def pathSum(self, root, sumx):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.list = []

        def helper(root, currlist, sumx):
            if root:
                currlist.append(root.val)
                if not root.left and not root.right:
                    if sum(currlist) == sumx:
                        self.list.append(copy.deepcopy(currlist))
                if root.left:
                    helper(root.left, currlist, sumx)

                if root.right:
                    helper(root.right, currlist, sumx)
                currlist.pop()

        if root:
            helper(root, [], sumx)
        else:
            return []
        return self.list