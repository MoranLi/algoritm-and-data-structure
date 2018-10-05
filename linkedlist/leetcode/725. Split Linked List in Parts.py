class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def splitListToParts(root, k):
    """
    :type root: ListNode
    :type k: int
    :rtype: List[ListNode]
    """
    listx = []
    listy = []
    count = 0
    x = root
    while x != None:
        listx.append(x)
        count += 1
        x = x.next
    sizebase = count / k
    extra = count % k
    if extra > 0:
        sizebase+=1
    i = 0
    while i < count:
        listz = []
        if extra > 0:
            for j in range(i,i+sizebase):
                listz.append(listx[j].val)
            extra-=1
            i += sizebase
            if extra == 0:
                sizebase-=1
        else:
            for j in range(i,i+sizebase):
                listz.append(listx[j].val)
            i += sizebase
        listy.append(listz)
    while len(listy) < k:
        listy.append([])
    return listy

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

print (splitListToParts(a,3))