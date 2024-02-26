import math

# Exercicio 1
altura = float(input("Digite a largura: "))
largura = float(input("Digite a altura: "))
print(f"Area = {largura * altura}")

# Exercicio 2
tamanho = float(input("Digite o tamanho do quadrado"))
print(f"Area = {tamanho * tamanho}")

# Exercicio 3
diagonal = float(input("Digite a diagonal: "))
print(f"O tamanho do quadrado eh: {math.ceil(diagonal / math.sqrt(2))}")

# Exercicio 4
base = float(input("Base? "))
altura = float(input("Altura? "))
print(f"A Area eh: {(base * altura) / 2 }")

# Exercicio 5
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

print(f"Media: {(n1 + n2 + n3 + n4) / 4}")

# Exercicio 6
milha_maritima = float(input("Digite a quantidade de milhas maritimas: "))
milha_maritima_em_kms = milha_maritima * 1.852
print(f"{milha_maritima} em kilometros sao: {milha_maritima_em_kms}")

# Exercicio 7
dolares = float(input("Quantidade de dolares: "))
quotacao = float(input("Quotacao Dolar/Real: "))
print(f"${dolares} sao R${dolares * quotacao}")

# # Exercicio 8
x = float(input("Quanto eh X? "))
y = float(input("Quanto eh Y? "))
print(f"X^Y eh igual a: {math.pow(x,y)}")

# Exercicio 9


# Exercicio 10

a = float(input("Quanto eh A: "))
b = float(input("Quanto eh B: "))
if a > b:
    print(f"A eh maior que B, e seu valor eh {a}")
elif b > a:
    print(f"B eh maior que A, e seu valor eh {a}")
else:
    print(f"Empate! os valores sao iguais: {a}")

# Exercicios 13 e 14
largura = float(input("Quanto de largura tem o terreno? "))
altura = float(input("Quanto de altura tem o terreno? "))
if largura * altura > 100:
    print("Terreno Grande!")
else:
    print("Terreno Pequeno.")

# Exercicio 16
# https://mundoeducacao.uol.com.br/matematica/condicao-existencia-um-triangulo.htm#:~:text=S%C3%B3%20ir%C3%A1%20existir%20um%20tri%C3%A2ngulo,soma%20dos%20outros%20dois%20lados.
lado_a = float(input("Quanto eh o lado A? "))
lado_b = float(input("Quanto eh o lado B? "))
lado_c = float(input("Quanto eh o lado C? "))

cond1 = abs(lado_b - lado_c) < lado_a < lado_b + lado_c
cond2 = abs(lado_a - lado_c) < lado_b < lado_a + lado_c
cond3 = abs(lado_a - lado_b) < lado_c < lado_a + lado_b

# if (lado_a + lado_b) >= lado_c or (lado_b + lado_c) >= lado_a or lado_c + lado_a > lado_b:
if cond1 and cond2 and cond3:
    if lado_a == lado_b == lado_c:
        print("Eh um triangulo equilatero!")
    elif lado_a != lado_b != lado_c:
        print("Eh um triangulo escaleno!")
    else:
        print("Eh um triangulo isosceles")
else:
    print("Nao eh um triangulo")

# Exercicio 17
# Triangulo retangulo: a^2 = b^2 + c^2
lado_a = float(input("Quanto eh o lado A? "))
lado_b = float(input("Quanto eh o lado B? "))
lado_c = float(input("Quanto eh o lado C? "))

quad_a = math.pow(lado_a, 2)
quad_b = math.pow(lado_b, 2)
quad_c = math.pow(lado_c, 2)

cond1 = abs(lado_b - lado_c) < lado_a < lado_b + lado_c
cond2 = abs(lado_a - lado_c) < lado_b < lado_a + lado_c
cond3 = abs(lado_a - lado_b) < lado_c < lado_a + lado_b

if cond1 and cond2 and cond3:
    c1 = quad_a == quad_b + quad_c
    c2 = quad_b == quad_a + quad_c
    c3 = quad_c == quad_a + quad_b
    if c1 or c2 or c3:
        print("Eh um triangulo retangulo!")
    else:
        print("Nao eh um triangulo retangulo")
else:
    print("Nao eh um triangulo")

# Exercicio 18
p1 = float(input("Quanto tirou na p1? "))
p2 = float(input("Quanto tirou na p2? "))
media = (p1 + 2*p2) / 3
print(f"Sua media eh {media}")

if media >= 5:
    print("Aprovado!")
else:
    print("Reprovado!")


# Exercicio 19
p1 = float(input("Quanto tirou na p1? "))
quanto_de_nota_pra_fechar = (5 * 3 - p1) / 2
print(f"Voce precisa de: {quanto_de_nota_pra_fechar} na P2")
