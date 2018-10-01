import random

def partition_before(listx,partition):
  for a in range(0,len(listx)):
    if listx[a] < partition:
      ele = listx.pop(a)
      listx.insert(0,ele)
  return listx

list1 = []
for x in range(0,10):
  list1.append(random.randint(0,5))

print(list1)
print(partition_before(list1,2))