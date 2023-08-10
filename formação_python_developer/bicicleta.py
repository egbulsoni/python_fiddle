class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("beep beeeep...")

    def parar(self):
        print("vrrrrp")

    def correr(self):
        print("vruum vruum")


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
b2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(b2)
