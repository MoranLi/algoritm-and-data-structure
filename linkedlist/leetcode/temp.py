class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

x = ListNode(1)
y = ListNode(2)
z = ListNode(3)

print(a==x)

x.next = y
y.next = z

print(a == x)

b.next = None

print (a==x)