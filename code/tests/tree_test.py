from objects.list_structures.binary_search_tree import BinarySearchTree
import random

a = BinarySearchTree()
a.add(10)
a.add(9)
a.add(11)
a.add(12)
a.add(8)
a.add(7)
a.add(13)
print("traverse")
for b in a.traverse():
    print(b)
print("traverse")
print(a.head)
print("Height: " + str(a.count()))
print(a.head.prev, a.head.next)

print(a.max())
print(a.min())

print(0 in a)
print(a.head)
print([b for b in a.traverse()])
print(a.height())
