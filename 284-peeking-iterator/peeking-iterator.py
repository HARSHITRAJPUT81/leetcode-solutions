# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def hasNext(self): ...
#     def next(self): ...

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_element = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.next_element

    def next(self):
        val = self.next_element
        self.next_element = (
            self.iterator.next() if self.iterator.hasNext() else None
        )
        return val

    def hasNext(self):
        return self.next_element is not None