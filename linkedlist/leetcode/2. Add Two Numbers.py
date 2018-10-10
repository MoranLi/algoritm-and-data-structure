class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        fake = ListNode(0)
        p3 = fake
        while p1 != None and p2 != None:
            v1 = p1.val + p2.val
            if v1 >= 10:
                v1 = v1 - 10
                if p1.next != None:
                    p1.next.val+=1
                elif p2.next != None:
                    p2.next.val+=1
                else:
                    p1.next = ListNode(1)
            vnode = ListNode(v1)
            p3.next = vnode
            p3 = vnode
            p1 = p1.next
            p2 = p2.next
        if p1 != None:
            value = p1.val
            pn = p1
            while value >= 10:
                pn.val-=10
                value-=10
                if pn.next != None:
                    pn.next.val+=1
                    value = pn.next.val
                else:
                    pn.next = ListNode(1)
                pn = pn.next
            p3.next = p1
        if p2 != None:
            value = p2.val
            pn = p2
            while value >= 10:
                pn.val-=10
                value-=10
                if pn.next != None:
                    pn.next.val+=1
                    value = pn.next.val
                else:
                    pn.next = ListNode(1)
                pn = pn.next
            p3.next = p2
        return fake.next