class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        p0 = ListNode(0)
        p1 = head
        p2 = head.next
        p3 = p2.next
        p2.next = p1
        p1.next = p3

        p0.next = p2

        p1.next = self.swapPairs(p3)

        return p0.next
