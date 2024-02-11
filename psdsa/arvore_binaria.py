class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        # return str(self.root.value)
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
        list_of_traversed_tree = (list(map(int, (filter((' ').__ne__, self.__repr__())))))
        return list_of_traversed_tree == sorted(list_of_traversed_tree)

# Exemplo de uso
if __name__ == "__main__":
    # Construindo a árvore
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Criando a instância da árvore
    tree = Tree(root)

    # Imprimindo a representação da árvore
    print(tree)
    print(tree.is_balanced())

    raiz = Node(6)
    raiz.left = Node(4)
    raiz.left.right = Node(5)
    raiz.left.left = Node(2)
    raiz.left.left.left = Node(1)
    raiz.left.left.right = Node(3)
    raiz.right = Node(8)
    raiz.right.left = Node(7)
    raiz.right.right = Node(9)

    tree2 = Tree(raiz)
    print(tree2)
    print(tree2.is_balanced())
