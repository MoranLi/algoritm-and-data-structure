class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        beforeNodes = ListNode(0)
        afterNodes = ListNode(0)
        pb = beforeNodes
        pa = afterNodes
        p1 = head
        while p1 != None:
            val = p1.val
            temp = ListNode(val)
            if val >= x:
                pa.next = temp
                pa = temp
            else:
                pb.next = temp
                pb = temp
            p1 = p1.next
        pb.next = afterNodes.next
        return beforeNodes.next