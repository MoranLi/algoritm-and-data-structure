class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return None if head.val == val else head
        p1 = head
        # loop from second to one before last, to make sure there is no None value for pointers
        while p1 != None and p1.next != None:
            v1 = p1.next.val
            if v1 == val:
                p1.next = p1.next.next
            else:
                p1 = p1.next
        # check if first element is same as val
        if head.val == val:
            head = head.next
            # check if last element is same as val
            if head != None and head.val == val:
                head = head.next
        return head