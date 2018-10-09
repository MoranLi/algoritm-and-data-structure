class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        solution in one pass
        use a fast pointer point to nth node from start
        use other two pointer point to zero node(slow) and first node(mid)
        keep three pointer go until fast reach last
        that means the mid point to the node need to remove
        """
        fast = head
        while n > 0:
            n-=1
            fast = fast.next
        fake = ListNode(0)
        fake.next = head
        mid = fake.next
        slow = fake
        while fast != None:
            fast = fast.next
            slow = slow.next
            mid = mid.next
        slow.next = mid.next
        return fake.next