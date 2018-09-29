from sets import Set
import random
import copy

'''
Time:O(n)
Space:O(1)
use two pointer
when  pointer a is different from pointer b
means element between a and b is same to a
'''
def twopointer(listx):
  listx.sort()
  a = 0
  for b in range(1,len(listx)):
    if listx[a] != listx[b]:
      a+=1
      listx.insert(a,listx[b])
      del listx[a+1]
  return listx

def useSet(listx):
  listx = list(Set(listx))
  return listx

def doubleLoop(listx):
  for a in range(0,len(listx)):
    for b in range(a+1,len(listx)):
      if listx[a] == listx[b]:
        listx[b] = -1
  return listx
  
list1 = []
for x in range(0,10):
  list1.append(random.randint(0,5))
list2 = copy.deepcopy(list1)
print(list1)

list1 = twopointer(list1)
print(list1)

list1 = copy.deepcopy(list2)
list1 = useSet(list1)
print(list1)

list1 = copy.deepcopy(list2)
list1 = doubleLoop(list1)
print(list1)