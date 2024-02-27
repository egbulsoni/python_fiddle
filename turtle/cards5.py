import turtle

# Inicializar a tela e o cursor
tela = turtle.Screen()
cursor = turtle.Turtle()

# Definir uma função para desenhar retângulos
def desenhar_retangulo(x, y, largura, altura):
    cursor.penup()
    cursor.goto(x, y)
    cursor.pendown()
    for _ in range(2):
        cursor.forward(largura)
        cursor.right(90)
        cursor.forward(altura)
        cursor.right(90)

# Coordenadas do ponto de origem
x_origem = -50
y_origem = -50

# Tamanho dos retângulos
largura = 190
altura = 130

# Desenhar o primeiro retângulo em ângulo reto
desenhar_retangulo(x_origem, y_origem, largura, altura)

# Desenhar os próximos 4 retângulos inclinados a 30 graus
for i in range(1, 5):
    cursor.penup()
    cursor.goto(x_origem, y_origem)
    cursor.pendown()
    cursor.left(30 * i)  # Ajustar o ângulo para cada retângulo
    desenhar_retangulo(x_origem, y_origem, largura, altura)

# Manter a janela aberta até que ela seja fechada pelo usuário
tela.mainloop()
