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

# Coordenadas do retângulo original
x_original = -130 / 2
y_original = -190 / 2

# Desenhar o retângulo original
desenhar_retangulo(x_original, y_original, 130, 190)

# Coordenadas para os retângulos inclinados
x_inclinado = x_original
y_inclinado = y_original

# Definir uma função para desenhar retângulos inclinados a partir da ponta inferior esquerda do retângulo original
def desenhar_retangulos_inclinados(x, y, largura, altura, quantidade):
    for i in range(quantidade):
        cursor.penup()
        cursor.goto(x, y)
        cursor.pendown()
        cursor.left(30)  # Ângulo de inclinação
        desenhar_retangulo(x, y, largura, altura)
        # Atualizar as coordenadas para o próximo retângulo
        x += largura * 0.6  # Largura * cosseno(30 graus)
        y += altura * 1.2  # Altura * seno(30 graus)

# Desenhar os retângulos inclinados
desenhar_retangulos_inclinados(x_inclinado, y_inclinado, 130, 190, 5)

# Manter a janela aberta até que ela seja fechada pelo usuário
tela.mainloop()
