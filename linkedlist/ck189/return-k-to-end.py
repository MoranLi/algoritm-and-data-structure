import random

def return_k_to_end(list,k):
  return list[k:]

list1 = []
for x in range(0,10):
  list1.append(random.randint(0,5))

print(list1)
print(return_k_to_end(list1,5))