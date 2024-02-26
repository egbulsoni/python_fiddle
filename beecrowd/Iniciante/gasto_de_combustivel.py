tempo_gasto_viagem = int(input())
velocidade_media = int(input())
GASTO_DE_COMBUSTIVEL_EM_KM_POR_L = 12.0

distancia_da_viagem = tempo_gasto_viagem * velocidade_media
qtd_litros_gastos_na_viagem = distancia_da_viagem / float(GASTO_DE_COMBUSTIVEL_EM_KM_POR_L)

print("%.3f" % qtd_litros_gastos_na_viagem)