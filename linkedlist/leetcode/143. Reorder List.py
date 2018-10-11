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


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
        p1 = head
        count = 0
        while p1 != None:
            count += 1
            p1 = p1.next
        half = count / 2 - 1 if count % 2 == 0 else (count + 1) / 2 - 1
        p2 = head
        countT = 0
        while countT < half:
            p2 = p2.next
            countT += 1
        rp2 = reverseList(p2.next)
        p2.next = None
        p3 = head
        while rp2 != None:
            p4 = p3.next
            p5 = rp2.next
            p3.next = rp2
            rp2.next = p4
            p3 = p4
            rp2 = p5
