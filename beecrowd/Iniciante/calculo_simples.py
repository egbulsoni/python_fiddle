linha1 = list(map(float, input().split()))
linha2 = list(map(float, input().split()))

total_linha1 = linha1[1] * linha1[2]
total_linha2 = linha2[1] * linha2[2]
print("VALOR A PAGAR: R$ %.2f" % (total_linha1 + total_linha2))
