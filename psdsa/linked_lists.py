

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

# my impl of the pop method
    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     elif self.length == 1:
    #         val = self.head.value
    #         self.head = None
    #         self.tail = None
    #         self.length = 0
    #         return val
    #     else:
    #         temp = self.head
    #         # print(temp.next.next.next.value)
    #         while temp.next.next is not None:
    #             temp = temp.next
    #         temp.next = None
    #         val = self.tail.value
    #         self.tail = temp
    #         self.length -= 1
    #         return val

# instr solution
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

# my solution
    # def pop_first(self):
    #     if self.length == 0:
    #         return None
    #     elif self.length == 1:
    #         temp = self.head
    #         self.head = None
    #         self.tail = None
    #     else:
    #         temp = self.head
    #         self.head = self.head.next
    #     temp.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.tail = None
    #     return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

# instr solution
    def pop_first(self):
        if self.length == 0:
            return None
        val = self.head
        self.head = self.head.next
        val.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return val

# my solution
# actually coded an insert
    # def set_value(self, index, value):
    def insert_at(self, value, index):
        new_node = Node(value)
        temp = self.head
        if index > self.length or index < 0:
            return False
        if index == 0:
            # new_node.next = self.head
            # self.head = new_node
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        for _ in range(index - 1):
            temp = temp.next
        pre = temp
        pre = pre.next
        temp.next = new_node
        new_node.next = pre
        self.length += 1
        return True

# instr solution
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index - 1)
        cur = temp.next
        prox = cur.next
        cur.next = None
        temp.next = prox
        self.length -= 1
        return cur

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# my_linked_list = LinkedList(4)
# my_linked_list.append(2)

# my_linked_list.append(15)
# my_linked_list.append(7)

# my_linked_list.prepend(3)
# # my_linked_list.print_list()

# my_linked_list.print_list()

# for i in range(0, 5):
#     print(my_linked_list.pop())


# my_linked_list.print_list()
# for i in range(0, 5):
#     my_linked_list.pop_first()
#     my_linked_list.print_list()
# ll2 = LinkedList(3)
# ll2.print_list()
# ll2.pop()
# ll2.print_list()
# ll2.pop()
# ll2.print_list()
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.reverse()
my_linked_list.print_list()

# my_linked_list.print_list()
# # print(my_linked_list.get(3))
# my_linked_list.set_value(2, 7)
# my_linked_list.print_list()

# my_linked_list.set_value(5, 17)
# my_linked_list.print_list()

# my_linked_list.set_value(0, 23)
# my_linked_list.print_list()

# my_linked_list.remove(4)
# my_linked_list.print_list()

# ll = LinkedList(11)
# ll.append(3)
# ll.append(23)
# ll.append(7)

# print("o node removido foi: ", ll.remove(2), '\n')
# ll.print_list()
