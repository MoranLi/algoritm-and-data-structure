# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(array,left,right):
            if right == left:
                return None
            else:
                mid = (right-left)/2 if (right-left)%2 == 0 else (right-left-1)/2
                root = TreeNode(array[mid])
                root.left = helper(root.left,array,left,mid)
                root.right = helper(root.right,array,mid+1,right)
                return root
        root = None
        root = helper(nums,0,len(nums))
        return root

solution = Solution()

a = [1,2,3,4,5,6,7]
solution.sortedArrayToBST(a)