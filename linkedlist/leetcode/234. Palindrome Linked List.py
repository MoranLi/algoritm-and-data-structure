class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
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
"""
Time complexity: O(2.5n)
Space complexity: O(1)
go to the mid of list(1.5n), reverse it(0.5n) and compare it with from head(0.5n)
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pm = head
        count = 0
        while pm != None:
            count+=1
            pm = pm.next
        mid = count / 2 if count % 2 == 0 else (count - 1) / 2
        newcount = 0
        pm = head
        while newcount < mid:
            pm = pm .next
            newcount +=1
        if count % 2 != 0:
            pm = pm.next
        pmr = reverseList(pm)
        ph = head
        while pmr != None and ph != None:
            if pmr.val != ph.val:
                return False
            pmr = pmr.next
            ph = ph.next
        return True