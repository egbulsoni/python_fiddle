from collections import OrderedDict

if __name__ == '__main__':
    dicio = {}
    arr = list()
    # popula um dicionario, como nomes e pontuações
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dicio[name] = score
    # Ordena um dicionario
    sorted_dict = OrderedDict(dicio)
    # printa chave e valor
    for key in sorted_dict.keys:
        print(key)
    for value in sorted_dict.values:
        print(value)
    #falta achar como faz pra pegar o segundo menor valor