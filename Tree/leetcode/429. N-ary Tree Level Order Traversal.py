class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        def helper(root, depth, listx):
            if depth > len(listx):
                listx.append([])
            for i in root.children:
                helper(i, depth + 1, listx)
            listx[depth - 1].append(root.val)

        listx = []
        if root:
            helper(root, 1, listx)
        else:
            return []
        return listx
