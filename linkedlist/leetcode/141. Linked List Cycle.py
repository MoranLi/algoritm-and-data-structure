# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        walk = head
        run = head
        while walk != None and run != None and run.next != None:
            walk = walk.next
            run = run.next.next
            if walk == run:
                return True
        return False