class Stack:
    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        try:
            return self._storage.pop()
        except IndexError:
            raise IndexError("The stack is empty.")
