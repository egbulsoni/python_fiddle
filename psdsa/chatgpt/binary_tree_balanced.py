class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return self._traverse_in_order(self.root)

    def _traverse_in_order(self, node):
        if node:
            arvore = ''
            arvore += self._traverse_in_order(node.left)
            arvore += str(node.value) + ' '
            arvore += self._traverse_in_order(node.right)
            return arvore
        return ''

    def is_balanced(self):
        list_of_traversed_tree = list(map(int, filter((' ').__ne__, self.__repr__().split())))
        return list_of_traversed_tree == sorted(list_of_traversed_tree)

    def collect_values(self, node, values):
        if node:
            self.collect_values(node.left, values)
            values.append(node.value)
            self.collect_values(node.right, values)

    def balancear(self):
        values = []
        self.collect_values(self.root, values)
        values.sort()
        self.root = self.construct_tree(values, 0, len(values) - 1)

    def construct_tree(self, values, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = Node(values[mid])
        node.left = self.construct_tree(values, start, mid - 1)
        node.right = self.construct_tree(values, mid + 1, end)
        return node


# Exemplo de uso:
# Crie a árvore original
# root = Node(5)
# root.left = Node(3)
# root.right = Node(8)
# root.left.left = Node(1)
# root.right.left = Node(6)
# root.right.right = Node(9)

root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.right = Node(5)
root.left.left = Node(4)
root.left.left.left = Node(6)
root.left.left.left.left = Node(7)


tree = Tree(root)
print("Árvore original:", tree)

# Verifica se a árvore está balanceada
print("Árvore balanceada?", tree.is_balanced())

# Balanceia a árvore
tree.balancear()
print("Árvore balanceada:", tree)
print("Árvore balanceada?", tree.is_balanced())
