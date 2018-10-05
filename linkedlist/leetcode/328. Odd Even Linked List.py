class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None:
        return head
    if head.next == None:
        return head
    p1 = head
    p2 = head.next
    p0 = p2
    while p1.next.next != None and p2.next.next != None:
        p3 = p1.next.next
        p4 = p2.next.next
        p1.next = p3
        p2.next = p4
        p1 = p1.next
        p2 = p2.next
    if p1.next.next != None:
        p1.next = p1.next.next
        p1 = p1.next
    p2.next = None
    p1.next = p0
    return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

oddEvenList(a)