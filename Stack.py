class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


s = Stack()
s.push(1)
s.push(2)
print(s.pop)

