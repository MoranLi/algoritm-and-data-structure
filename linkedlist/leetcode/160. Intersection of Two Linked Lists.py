class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        countA = 0
        countB = 0
        pa = headA
        pb = headB
        while pa !=None:
            pa = pa.next
            countA+=1
        while pb != None:
            pb = pb.next
            countB+=1
        paa = headA
        pbb = headB
        lengthDiff = max(countA,countB) - min(countA,countB)
        if countA < countB:
            countx = 0
            while countx < lengthDiff and pbb != None:
                pbb = pbb.next
                countx+=1
        elif countA > countB:
            countx = 0
            while countx < lengthDiff and paa != None:
                paa = paa.next
                countx+=1
        while paa != None and pbb != None:
            if paa.val == pbb.val:
                return paa
            paa = paa.next
            pbb = pbb.next
        return None