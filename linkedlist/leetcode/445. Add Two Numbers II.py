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


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = reverseList(l1)
        l4 = reverseList(l2)
        end = None
        a = 0
        while l3 != None and l4 != None:
            a = l3.val + l4.val
            if a >= 10:
                a -= 10
                if l3.next != None:
                    l3.next.val += 1
                elif l4.next != None:
                    l4.next.val += 1
                else:
                    l3.next = ListNode(1)
            x = ListNode(a)
            x.next = end
            end = x
            l3 = l3.next
            l4 = l4.next
        if l3 != None:
            z = l3
            if a >= 10:
                z.val += 1
            while z.next != None:
                if z.val >= 10:
                    z.val -= 10
                    z.next.val += 1
                z = z.next
            if z.next == None and z.val >= 10:
                y = ListNode(1)
                z.next = y
                z.val -= 10
            l5 = reverseList(l3)
            k = l5
            while k.next != None:
                k = k.next
            k.next = end
            end = l5
        if l4 != None:
            z = l4
            if a >= 10:
                z.val += 1
            while z.next != None:
                if z.val >= 10:
                    z.val -= 10
                    z.next.val += 1
                z = z.next
            if z.next == None and z.val >= 10:
                y = ListNode(1)
                z.next = y
                z.val -= 10
            l5 = reverseList(l4)
            k = l5
            while k.next != None:
                k = k.next
            k.next = end
            end = l5
        return end