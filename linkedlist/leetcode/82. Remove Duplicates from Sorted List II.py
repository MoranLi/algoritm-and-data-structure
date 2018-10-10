class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        fake = ListNode(0)
        fake.next = head
        p1 = fake
        p2 = head
        p3 = head.next
        while p3 != None:
            if p2.val != p3.val and p2.next != p3:
                p1.next = p3
                p2 = p3
            elif p2.val != p3.val:
                p1 = p1.next
                p2 = p2.next
            p3 = p3.next
        if p2.next != None and p3 == None:
            p1.next = None
        return fake.next

solution = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)
g = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

solution.deleteDuplicates(a)