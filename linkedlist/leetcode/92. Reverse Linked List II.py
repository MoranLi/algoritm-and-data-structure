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
    head = None
    end = None
    while pointer != None:
        v = pointer.val
        x = ListNode(v)
        if end == None:
            end = x
        x.next = head
        head = x
        pointer = pointer.next
    return head,end

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        fake = ListNode(0)
        countstart = 0
        countend = 0
        fake.next = head
        p1 = fake
        phead = None
        pbefore = fake
        pafter = None
        while countend+1 < n:
            if countstart+1 == m:
                pbefore = p1
                phead = p1.next
            p1 = p1.next
            countstart+=1
            countend+=1
        pafter = None if p1.next == None else p1.next.next
        if p1.next != None and p1.next.next != None:
            p1.next.next = None
        newhead, newend = reverseList(phead)
        pbefore.next = newhead
        newend.next = pafter
        return fake.next

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

