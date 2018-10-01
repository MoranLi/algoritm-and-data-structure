# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list = []
        pointer1 = head
        while(pointer1 != None):
            list.append(pointer1)
            pointer1 = pointer1.next
        if len(list)%2 == 0:
            return list[int(round(len(list)/2))]
        else:
            return list[int(round((len(list)-1)/2))]