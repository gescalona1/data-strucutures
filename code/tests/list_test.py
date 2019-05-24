from objects.list_structures.linked_list import LinkedList
import random

nlist: LinkedList = LinkedList()
nlist.append(1)
nlist.append(2)
nlist.append(3)
print(nlist.peek(), 1)  # ({}:1:2) 1
print(nlist.head.data)  # 1
print(nlist)  # 1,2,3
nlist.insert(1, 4)
print(nlist)  # 1,4,3,2
nlist.remove(2)
print(nlist)  # 1,4,3
print(len(nlist))  # 3

nlist.sort("bubble")
print(nlist)


random_list: LinkedList = LinkedList()
for l in range(15):
    random_list.append(random.randint(0, 100))
print("New Randomizer List to sort:")
print(random_list)
random_list.sort("bubble")
print("After sorting:")
print(random_list)
print(random_list[2])
