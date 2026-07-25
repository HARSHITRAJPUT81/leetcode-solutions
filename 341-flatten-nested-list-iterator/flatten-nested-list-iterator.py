class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True

            self.stack.pop()
            self.stack.extend(top.getList()[::-1])

        return False