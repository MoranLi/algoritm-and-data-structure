# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.list = [root.val]

        def cursor(root):
            if root:
                if root.val not in self.list:
                    if len(self.list) == 1:
                        self.list.append(root.val)
                    else:
                        if root.val < self.list[1] and root.val > self.list[0]:
                            self.list[1] = root.val
                cursor(root.left)
                cursor(root.right)

        cursor(root)
        return self.list[1] if len(self.list) > 1 else -1


