from typing import Union, Any


class Node:
    def __init__(self, prev, data: Any, nxt):
        self._prev = prev
        self._nxt = nxt
        self._data = data

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value):
        self._prev = value

    @property
    def next(self):
        return self._nxt

    @next.setter
    def next(self, value):
        self._nxt = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __str__(self):
        prev_data = "{}"
        next_data = "{}"
        if self.prev is not None:
            prev_data = self.prev.data
        if self.next is not None:
            next_data = self.next.data
        return f"({prev_data}:{self.data}:{next_data})"
