# Exercicio 1
def recebe_valor_positivo():
    while True:
        i = int(input("Digite um valor inteiro positivo: "))
        if i >= 0:
            print(f"Seu valor eh: {i}")
            break

# recebe_valor_positivo()

# Exercicio 2
def smp():
    a = float(input("Digite o primeiro valor: "))
    while True:
        b = float(input("Digite o segundo valor: "))
        if b > a:
            break


# Exercicio 3:
def sexo():
    while True:
        s = str(input("Voce eh Homem(M) ou Mulher(F)? "))
        if s == 'M' or s == 'm' or s == 'F' or s == 'f':
            print("Boa!")
            break

# sexo()


# Exercicio 4
def tabuada():
    for i in range(1, 11):
        print(f"{i} * 5 = {i * 5}")


# Exercicio 5
def numero_pra_tabuada():
    while True:
        i = int(input("Digite o numero pra tabuada: "))
        if i >= 0:
            break
    for n in range(1, 11):
        print(f"{i} * {n} = {i * n}")


# Exercicio 6
def tabuada_do_numero_x_de_b_para_a():
    while True:
        x = int(input("Qual o numero da tabuada? "))
        if x > 0:
            break
    while True:
        a = int(input("Qual o valor inicial do intervalo?"))
        b = int(input("Qual o valor final do intervalo?"))
        if b > a:
            break
    for i in range(b, a - 1, -1):
        print(f"{x} * {i} = {x * i}")



# Exercicio 7
def tabuada_de_1_a_20_no_intervalo_de_1_a_10():
    for i in range(1, 21):
        for n in range(1,11):
            print(f"{i} * {n} = {i * n}")
            if n == 10:
                _ = input()
                continue


# Exercicio 8
def soma_inteiros_positivos_de_1_a_100():
    acc = 0
    for i in range(1,101):
        acc += i
    return acc


def fibo(n):
    n = int(n)
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)


# for i in range(0, 6):
#     print(fibo(i))

def lista_de_fibo(n):
    ls = []
    for i in range(n):
        ls.append(fibo(i))
    return ls

# print(lista_de_fibo(30))


def entrar_10_valores_positivos():
    ls = []
    while len(ls) < 10:
        n = int(input(f"Digite um numero "))
        if n < 0:
            print("valor errado, digite novamente")
            continue
        ls.append(n)
    print(f"maior valor: {max(ls)}")
    print(f"a soma dos valores: {sum(ls)}")
    print(f"media aritmetica: {sum(ls) / len(ls)}")
    return ls

# lista = entrar_10_valores_positivos()
# print(lista)


def verifica_numero_positivo(num):
    return num > 0


def verifica_numero_negativo(num):
    return num < 0


def entrar_n_valores_positivos():
    ls = []
    while True:
        tamanho = int(input("quanto eh n? "))
        if 0 < tamanho < 20:
            break

    while len(ls) < tamanho:
        n = int(input(f"Digite um numero "))
        ls.append(n)
    print(f"maior valor: {max(ls)}")
    print(f"menor valor: {min(ls)}")
    print(f"a soma dos valores: {sum(ls)}")
    print(f"media aritmetica: {sum(ls) / len(ls)}")
    print(f"porcentagem dos positivos: {(len(list(filter(verifica_numero_positivo,ls))) / len(ls)) * 100}%")
    print(f"porcentagem dos negativos: {(len(list(filter(verifica_numero_negativo,ls))) / len(ls)) * 100}%")
    return ls


# print(entrar_n_valores_positivos())
def entrar_n_valores_positivos_s_n():
    while True:
        ls = []
        while True:
            tamanho = int(input("quanto eh n? "))
            if 0 < tamanho < 20:
                break

        while len(ls) < tamanho:
            n = int(input(f"Digite um numero "))
            ls.append(n)
        print(f"maior valor: {max(ls)}")
        print(f"menor valor: {min(ls)}")
        print(f"a soma dos valores: {sum(ls)}")
        print(f"media aritmetica: {sum(ls) / len(ls)}")
        print(f"porcentagem dos positivos: {(len(list(filter(verifica_numero_positivo,ls))) / len(ls)) * 100}%")
        print(f"porcentagem dos negativos: {(len(list(filter(verifica_numero_negativo,ls))) / len(ls)) * 100}%")

        # Continuar?
        print("Deseja uma nova execução do programa?")
        opc = input("S/N: ")
        if opc == "n" or opc == "N":
            break
        elif opc == "s" or opc == "S":
            continue


# entrar_n_valores_positivos_s_n()
def fat_funcao_calculo(n):
    if n <= 1:
        return 1
    else:
        return n * fat_funcao_calculo(n - 1)


def fat_funcao_entrada():
    while True:
        num = int(input("Fatorial de quanto? "))
        if num >= 0:
            break
        else:
            print("Erro! deve ser informado apenas numeros positivos")
    print(fat_funcao_calculo(num))
    while True:
        opc = input("Deseja fazer mais operacoes? (S/N): ")
        if opc == 'S' or opc == 's':
            fat_funcao_entrada()
            break
        elif opc == 'N' or opc == 'n':
            break
        else:
            print("opcao invalida")


fat_funcao_entrada()