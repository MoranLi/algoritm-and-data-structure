# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

'''
only need random pointer point to a node with same label but not exactly same node
'''

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        nodeDict = {}
        p1 = head
        while p1 != None:
            nodeDict[p1.label] = RandomListNode(p1.label)
            p1 = p1.next
        fake = RandomListNode(0)
        p4 = fake
        p2 = head
        while p2 != None:
            x = RandomListNode(p2.label)
            if p2.random == None:
                x.random == None
            else:
                x.random = nodeDict[p2.random.label]
            p4.next = x
            p4 = x
            p2 = p2.next
        return fake.next