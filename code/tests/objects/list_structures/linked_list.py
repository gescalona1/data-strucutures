from .node import Node
from typing import *


class LinkedList(list):

    def __init__(self):
        list.__init__(self)
        self._head_node = None

    @property
    def head(self) -> Node:
        """Get the head node of this list"""
        return self._head_node

    @head.setter
    def head(self, node: Node):
        self._head_node = node

    def append(self, data: Any):
        """This method is the equivalent of add in other languages"""
        if self._head_node is None:
            self._head_node = Node(None, data, None)
            return
        curr: Node = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(curr, data, None)

    def insert(self, index: int, data: Any):
        i = 0
        for node in self._loop():
            if i == index:  # [1]-->[2]-->[3] --- insert(1, 4)
                #  I could've just switched the data values and make a new node at the end
                new_node: Node = Node(node.prev, data, node)
                previous: Node = node.prev
                nextious: Node = node.next
                previous.next = new_node
                nextious.prev = node

                node.prev = new_node

                break
            i += 1

    def remove(self, index: int):
        i = 0
        for node in self._loop():
            if i == index:
                node.prev.next = node.next
                node.next.prev = node.prev
                break
            i += 1

    def peek(self) -> Node:
        return self._head_node

    def __len__(self) -> int:
        """len(LinkedList) returns the length of the list"""
        i = 0
        for node in self._loop():
            i += 1
        return i

    def __contains__(self, item: Any) -> bool:
        """`item` in LinkedLIst returns if list contains `item`"""
        for node in self._loop():
            if node.data == item:
                return True
        return False

    def _loop(self):
        curr: Node = self._head_node
        while curr.next is not None:
            yield curr
            curr: Node = curr.next
        yield curr

    def __getitem__(self, key: int):
        i = 0
        for node in self._loop():
            if i == key:
                return node.data
            i += 1
        return None

    def __str__(self):
        all_nodes = [str(val.data) for val in self._loop()]
        return ",".join(all_nodes)

    def sort(self, me: str):  # Assumes that the datas will be numbers
        if me == "bubble":
            length = self.__len__()
            for node in range(length):
                for node in self._loop():
                    if node.next is not None and node.data > node.next.data:
                        # Node: [1,4,3] node
                        # Node: [4,3,5] node.next
                        # make new nodes (instead of switching them around)?
                        temp = node.data
                        node.data = node.next.data
                        node.next.data = temp
