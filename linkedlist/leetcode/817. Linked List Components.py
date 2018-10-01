# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        """
        O(N) solution
        exceed time limit
        pointer = head 
        count = 0
        conti = False
        while pointer != None:
            if pointer.val in G:
                conti = True
            else:
                if conti == True:
                    count+=1
                    conti = False
            pointer = pointer.next
        if conti == True:
            count+=1
        return count
        """
        Gset = set(G)
        cur = head
        ans = 0
        while cur:
            if (cur.val in Gset and
                    getattr(cur.next, 'val', None) not in Gset):
                ans += 1
            cur = cur.next

        return ans