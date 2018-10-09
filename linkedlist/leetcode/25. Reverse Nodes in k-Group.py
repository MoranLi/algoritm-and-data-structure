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
    return head, end

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 1
        fake = ListNode(0)
        p1 = head
        phead = head
        fake.next = p1
        pbefore = fake
        while p1 != None:
            if count == k:
                pnext = p1.next
                p1.next = None
                head,end = reverseList(phead)
                pbefore.next = head
                end.next = pnext
                pbefore = end
                phead = pnext
                p1=pnext
                count = 1
            else:
                p1 = p1.next
                count+=1
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
