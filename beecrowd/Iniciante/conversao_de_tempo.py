duracao_em_segundos = int(input())
horas = int(duracao_em_segundos / 3600)
resto = int(duracao_em_segundos % 3600)
minutos = int(resto / 60)
resto = int(duracao_em_segundos % 60)
segundos = int(resto)

# print(horas)
# print(minutos)
# print(segundos)
print(f"{horas}:{minutos}:{segundos}")