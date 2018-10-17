from TreeNode import TreeNode


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def helper(root, string):
            if root:
                string += '('
                string += str(root.val)
                if root.left:
                    string += helper(root.left, '')
                else:
                    if root.right:
                        string += "()"
                if root.right:
                    string += helper(root.right, '')
                string += ')'
                return string

        string = ''
        if t:
            string = helper(t, '')
        string = string[1:len(string) - 1]
        return string


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
b.right = d

solution = Solution()

print(solution.tree2str(a))