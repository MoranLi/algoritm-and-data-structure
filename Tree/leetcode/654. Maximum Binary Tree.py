import sys
from TreeNode import TreeNode

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        maxi = -sys.maxint - 1
        index = 0
        for i in range(0, len(nums)):
            if maxi < nums[i]:
                maxi = nums[i]
                index = i
        root = TreeNode(maxi)
        root.left = self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:len(nums)])
        return root


nums = [3,2,1,6,0,5]

solution = Solution()

root = solution.constructMaximumBinaryTree(nums)
print(1)