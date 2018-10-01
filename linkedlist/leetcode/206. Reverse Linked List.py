# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer = head
        end = None
        while pointer != None:
            v = pointer.val
            x = ListNode(v)
            x.next = end
            end = x
            pointer = pointer.next
        return end