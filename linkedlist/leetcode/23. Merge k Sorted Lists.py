import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        i = 0
        while i < len(lists):
            if lists[i] == None:
                del lists[i]
                i-=1
            i+=1
        if len(lists) == 0 :
            return None
        listheads = []
        for i in lists:
            listheads.append(i)
        fake = ListNode(0)
        p1 = fake
        while listheads != []:
            minval = sys.maxint
            minindex = 0
            for i in range(0,len(listheads)):
                if minval > listheads[i].val:
                    minval = listheads[i].val
                    minindex = i
            minNode = ListNode(minval)
            p1.next = minNode
            p1 = minNode
            listheads[minindex] = listheads[minindex].next
            if listheads[minindex] == None:
                del listheads[minindex]
        return fake.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
h = ListNode(8)
k = ListNode(9)

a.next = b
b.next = c

d.next = e
e.next = f

g.next = h
h.next = k

solution = Solution()
solution.mergeKLists([a,d,g])