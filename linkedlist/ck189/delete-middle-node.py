import random

def delete_middle(listx):
  del listx[len(listx)/2]
  return listx

list1 = []
for x in range(0,10):
  list1.append(random.randint(0,5))

print(list1)
print(delete_middle(list1))