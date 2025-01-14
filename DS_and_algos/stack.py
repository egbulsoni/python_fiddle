class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Pilha():
    def __init__(self, node):
        self.length = 1
        self.head = node

    def __str__(self):
        pilha = ""
        temp = self.head
        while temp:
            pilha += str(temp.value) + "->"
            temp = temp.next
        pilha += "None"
        return pilha
            
    def push(self, node):
        self.length += 1
        node.next = self.head
        self.head = node

    def pop(self):
        self.length -= 1
        removed = self.head
        self.head = self.head.next
        return removed


n1 = Node(3)
n2 = Node(4)
n3 = Node(5)
p = Pilha(n1)
p.push(n2)
p.push(n3)
print(p)
p.pop()
print(p)
p.pop()
print(p)
p.pop()
print(p)
