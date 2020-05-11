# class implementation is based on Data Structures and Algorithms Using Python – R. Necaise

from modules.abstract_collection import Node, AbstractCollection


class LinkedQueue(AbstractCollection):
    """
    A link-based queue implementation.
    """

    def __init__(self, sourceCollection=None):
        self._front = self._rear = None
        AbstractCollection.__init__(self, sourceCollection)

    def __iter__(self):
        """
        Make LinkedQueue iterable.
        """
        cursor = self._front
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def peek(self):
        """
        Returns the item at the front of the queue.
        """
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self._front.data

    def clear(self):
        """
        Makes queue empty.
        """
        self._size = 0
        self._front = self._rear = None

    def add(self, item):
        """
        Adds item to the rear of the queue.
        """
        newNode = Node(item, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        """
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

    def remove(self, index):
        """
        Removes and returns the item at index.
        """
        if index < 0 or index >= len(self):
            raise AttributeError("i must be >= 0 and < size of queue")
        if index == 0:
            oldItem = self._front.data
            self._front = self._front.next
        else:
            probe = self._front
            while index > 1:
                probe = probe.next
                index -= 1
            oldItem = probe.next.data
            probe.next = probe.next.next
        self._size -= 1
        if self.isEmpty():
            self._rear = None
        return oldItem
