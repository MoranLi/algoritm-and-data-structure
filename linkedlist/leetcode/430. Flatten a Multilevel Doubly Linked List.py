# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        lists = []
        p1 = head
        l2 = Node(0,None,None,None)
        p2 = l2
        while p1 != None:
            temp = Node(p1.val,p2,None,None)
            p2.next = temp
            p2 = temp
            if p1.child != None:
                lists.append(p1.next)
                p1 = p1.child
            elif p1.next == None and lists != []:
                p1 = lists.pop()
            else:
                p1 = p1.next
        l2.next.prev = None
        return l2.next