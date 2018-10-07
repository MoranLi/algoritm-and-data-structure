# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

def insertionSortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    nlist = []
    p1 = head
    while p1 != None:
        nlist.append(p1.val)
        p1 = p1.next
    for index in range(1, len(nlist)):
        currentvalue = nlist[index]
        position = index
        while position > 0 and nlist[position - 1] > currentvalue:
            nlist[position] = nlist[position - 1]
            position = position - 1
        nlist[position] = currentvalue
    h2 = ListNode(nlist[0])
    x = h2
    for i in range(1,len(nlist)):
        y = ListNode(nlist[i])
        x.next = y
        x = y
    return h2

z = ListNode(0)
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

g.next = f
f.next = e
e.next = d
d.next = c
c.next = b
b.next = a
a.next = z

insertionSortList(g)