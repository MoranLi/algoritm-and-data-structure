class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None or k == 0:
            return head
        p1 = head
        count = 0
        while p1 != None:
            count += 1
            p1 = p1.next
        index = k % count
        if index == 0:
            return head
        unindex = count - index
        p2 = head
        countT = 0
        while countT < unindex - 1:
            p2 = p2.next
            countT += 1
        p3 = p2.next
        while p3.next != None:
            p3 = p3.next
        p3.next = head
        head2 = p2.next
        p2.next = None
        return head2

