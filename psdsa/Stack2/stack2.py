class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp.value
        # raise Exception("IndexError")
        return None
# my_stack = Stack(4)
# my_stack.pop()
# my_stack.pop()

# my_stack = Stack(4)
#
# my_stack.print_stack()
#
# my_stack.push(15)
# my_stack.push(3)
# my_stack.print_stack()
#
# my_s = Stack(3)
# my_s.push(32)
# my_s.print_stack()
# print('-----POPPIN\'------')
# print(my_s.pop())
# print(my_s.pop())
# print(my_s.pop())
# my_s.print_stack()
