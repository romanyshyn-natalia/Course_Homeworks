# classes implementation is based on Data Structures and Algorithms Using Python – R. Necaise


class Node:
    """
    Nodes for singly linked structures.
    """

    def __init__(self, data, next=None):
        """
        Instantiates a Node with default next of None.
        """
        self.data = data
        self.next = next


class AbstractCollection:
    """
    An abstract collection implementation.
    """

    def __init__(self, sourceCollection=None):
        """
        Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present.
        """
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __len__(self):
        """
        The number of items in self.
        """
        return self._size

    def isEmpty(self):
        """
        Check if a collection is empty.
        """
        return len(self) == 0

    def __str__(self):
        """Returns the string representation of self."""
        return ", ".join(map(str, self))

    def __add__(self, other):
        """
        Returns a new collection consisting of the
        items in self and other.
        """
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """
        Returns True if self equals other,
        or False otherwise.
        """
        if self is other:
            return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True
