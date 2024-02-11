import io
import unittest
from stack2 import Stack


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        s = Stack(5)
        self.assertEqual(s.pop(), 5)  # Testa se é possível fazer pop de um único elemento
        s.push(10)
        s.push(15)
        self.assertEqual(s.pop(), 15)  # Testa se o último elemento inserido é removido corretamente
        self.assertEqual(s.pop(), 10)  # Testa se o próximo elemento é removido corretamente
        self.assertIsNone(s.pop())  # Testa se a pilha está vazia

    def test_print_stack(self):
        s = Stack(20)
        s.push(25)
        s.push(30)
        s.push(35)

        # Redireciona a saída padrão para um buffer
        captured_output = io.StringIO()
        import sys
        sys.stdout = captured_output

        # Chama a função que imprime a pilha
        s.print_stack()

        # Restaura a saída padrão
        sys.stdout = sys.__stdout__

        # Obtém a saída capturada
        output = captured_output.getvalue()

        # Verifica se a saída corresponde à saída esperada
        expected_output = "35\n30\n25\n20\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
