# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def sumhelper(root, dictsum):
            if root:
                if root.left:
                    root.val += sumhelper(root.left, dictsum)
                if root.right:
                    root.val += sumhelper(root.right, dictsum)
                if root.val in dictsum:
                    dictsum[root.val] += 1
                else:
                    dictsum[root.val] = 1
                return root.val

        dictsum = {}
        sumhelper(root, dictsum)
        count = 1
        for i in dictsum:
            if dictsum[i] > count:
                count = dictsum[i]
        listy = []
        for i in dictsum:
            if dictsum[i] == count:
                listy.append(i)
        return listy



