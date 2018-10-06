class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        p1 = head
        p2 = head.next
        while p2 != None:
            if p1.val != p2.val:
                p1.next = p2
                p1 = p2
            p2 = p2.next
        if p1 != None:
            p1.next = None
        return head