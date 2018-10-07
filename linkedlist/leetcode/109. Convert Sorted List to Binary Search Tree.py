# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# TODO Recurion each level as root

def listToBST(list,start,end):
    if end == start:
        return TreeNode(list[start].val)
    if abs(end - start) == 1:
        small = TreeNode(list[start].val)
        large = TreeNode(list[end].val)
        if small == 0:
            large.left = small
            return large
        else:
            small.right = large
            return small
    else:
        midValue = (end-start)/2 if (end-start) %2 == 0 else (end-start-1)/2
        midValue+=start
        mid = TreeNode(list[midValue].val)
        mid.left = listToBST(list,start,midValue-1)
        mid.right = listToBST(list,midValue+1,end)
        return mid

def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    nlist = []
    p1 = head
    while p1 != None:
        nlist.append(p1)
        p1 = p1.next
    x = listToBST(nlist,0,len(nlist)-1)
    return x

z = ListNode(0)
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

z.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

sortedListToBST(z)