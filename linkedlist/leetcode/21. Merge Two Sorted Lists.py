class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    fs = ListNode(0)
    fp = fs
    l3 = l1
    l4 = l2
    while l3 != None and l4 != None:
        if l3.val < l4.val:
            ff = ListNode(l3.val)
            l3 = l3.next
        else:
            ff = ListNode(l4.val)
            l4 = l4.next
        fp.next = ff
        fp = fp.next
    if l3 != None:
        while l3 != None:
            ff = ListNode(l3.val)
            fp.next = ff
            fp = fp.next
            l3 = l3.next
    if l4 != None:
        while l4 != None:
            ff = ListNode(l4.val)
            fp.next = ff
            fp = fp.next
            l4 = l4.next
    return fs.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

a.next = b
b.next = c
#c.next = d
d.next = e
e.next = f
#f.next = g

mergeTwoLists(a,d)