class Stack():
    def __init__(self, value):
        self.ls = [value]

    def __str__(self):
        return str(self.ls)

    def push(self, value):
        self.ls.append(value)

    def peek(self):
        return self.ls[-1]

    def pop(self):
        self.ls = self.ls[:-1]


s = Stack(3)
s.push(4)
s.push(7)
print(s.peek())
print(s)
s.pop()
print(s)