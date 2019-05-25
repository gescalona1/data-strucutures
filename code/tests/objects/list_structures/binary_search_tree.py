from .node import Node
import math

class BinarySearchTree:
    """
    prev = left
    next = right
    """
    def __init__(self):
        self._head: Node = None

    @property
    def head(self):
        return self._head

    def add(self, data: int, *, node=None):
        empty_node = Node(None, data, None)
        if self._head is None:
            self._head = empty_node
            return
        if node is None:
            node = self._head
        if data <= node.data:
            if node.prev is not None and isinstance(node.prev, Node):
                self.add(data=data, node=node.prev)
                return
            else:
                node.prev = empty_node
        else:
            if node.next is not None and isinstance(node.next, Node):
                self.add(data=data, node=node.next)
                return
            else:
                node.next = empty_node

    def height(self, node: Node = None):
        temp = 0
        for count in self._find_height(self._head):
            if count > temp:
                temp = count
        return temp

    def _find_height(self, node: Node = None):
        if node is None:
            node = self._head
        counter: int = 0
        if node.prev is not None:
            counter = self._find_height(node.prev)
        else:
            counter += 1
        if node.next is not None:
            counter = self._find_height(node.next)
        else:
            counter += 1
        yield counter

    def count(self, node: Node = None) -> int:
        if node is None:
            node = self._head
        a, b = 0, 0
        if isinstance(node.prev, Node):
            a = self.count(node=node.prev)
        if isinstance(node.next, Node):
            b = self.count(node=node.next)
        return 1 + a + b

    def traverse(self, node: Node = None):
        if node is None:
            node: Node = self._head
        yield(node.data)
        if isinstance(node.prev, Node):
            yield from self.traverse(node.prev)
        if isinstance(node.next, Node):
            yield from self.traverse(node.next)

    def min(self):
        return min([item for item in self.traverse()])

    def max(self):
        return max([item for item in self.traverse()])

    def __contains__(self, item):
        for value in self.traverse():
            if value == item:
                return True
        return False
