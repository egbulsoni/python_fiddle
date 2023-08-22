# BINARY TREE
# Full tree => each node either
# points to 0 nodes or 2 nodes
# Perfect tree => any level in the tree that has any nodes is completely filled all the way across
# Complete tree => filling left to right with no gap s

# BINARY SEARCH TREE
# left nodes' value are less than the parent's value
# right nodes' value are more than the parent's value
# Big O
# search/remove/add: 2^ tree's node level
# in other words
# lookup, insert, remove: O(logn)
# worst case scenario, if straight line: O(n) (like a linked list)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# alternative constructor
# class BinarySearchTree:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.root = new_node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.contains(27))
print(my_tree.contains(17))
