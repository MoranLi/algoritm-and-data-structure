class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        implementation of quick sort
        loop through all nodes, group node smaller than head to a list and larger than head to another
        resort smaller list and larger list
        return it self until only one / none element left
        combine each step inrecursion
        """
        if head == None:
            return None
        if head.next == None:
            return head
        else:
            beforeNodes = ListNode(0)
            afterNodes = ListNode(0)
            equalNodes = ListNode(head.val)
            pb = beforeNodes
            pa = afterNodes
            pe = equalNodes
            p1 = head.next
            while p1 != None:
                temp = ListNode(p1.val)
                if p1.val < head.val:
                    pb.next = temp
                    pb = temp
                elif p1.val > head.val:
                    pa.next = temp
                    pa = pa.next
                else:
                    pe.next = temp
                    pe = temp
                p1 = p1.next
            sortbefore = self.sortList(beforeNodes.next)
            sortAfter = self.sortList(afterNodes.next)
            if sortbefore != None:
                psb = sortbefore
                while psb.next != None: psb = psb.next
                psb.next = equalNodes
            pe.next = sortAfter
            return sortbefore if sortbefore != None else equalNodes

solution = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

d.next = b
b.next = a
a.next = c

solution.sortList(d)
