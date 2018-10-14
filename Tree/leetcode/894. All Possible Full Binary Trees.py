from TreeNode import TreeNode
import copy


class Solution(object):
    def FBThelper(self, root, pos, N, lists):
        roots = copy.deepcopy(root)
        p1 = roots
        for c in pos:
            if c == "1":
                p1 = p1.left
            elif c == "2":
                p1 = p1.right
        node = p1
        if N >= 2:
            node.left = TreeNode(0)
            node.right = TreeNode(0)
            self.FBThelper(roots, pos+"1", N - 2, lists)
            self.FBThelper(roots, pos+"2", N - 2, lists)
            lists.append(root)
            return

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        lists = []
        root = TreeNode(0)
        self.FBThelper(root,"0", N - 1, lists)
        return lists


solution = Solution()

lists = solution.allPossibleFBT(7)

for each in lists:
    print(each.__str__(0))