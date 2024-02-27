import turtle

# Inicializar a tela e o cursor
tela = turtle.Screen()
cursor = turtle.Turtle()

# Definir uma função para desenhar retângulos inclinados
def desenhar_retangulos_inclinados(largura, altura, quantidade):
    # Desenhar o retângulo reto
    cursor.penup()
    cursor.goto(0, 0)
    cursor.pendown()
    for _ in range(2):
        cursor.forward(largura)
        cursor.right(90)
        cursor.forward(altura)
        cursor.right(90)

    # Definir as coordenadas da ponta inferior direita do retângulo reto
    x_inicial = largura / 2
    y_inicial = -altura / 2

    # Desenhar retângulos inclinados a 30 graus a partir da ponta inferior direita
    for _ in range(quantidade):
        cursor.penup()
        cursor.goto(x_inicial, y_inicial)
        cursor.pendown()
        cursor.left(30)  # Ângulo de inclinação
        for _ in range(2):
            cursor.forward(largura)
            cursor.right(90)
            cursor.forward(altura)
            cursor.right(90)
        # Atualizar as coordenadas para o próximo retângulo inclinado
        x_inicial += largura * 0.5  # Largura * cosseno(30 graus)
        y_inicial -= altura * 0.5  # Altura * seno(30 graus)

# Chamar a função para desenhar os retângulos inclinados
desenhar_retangulos_inclinados(130, 190, 5)

# Manter a janela aberta até que ela seja fechada pelo usuário
tela.mainloop()
