import math

ns = input()
ns = list(map(float, ns.split()))
a = ns[0]
b = ns[1]
c = ns[2]
triangulo = (a * c) / 2
circulo = (3.14159 * math.pow(c, 2))
trapezio = ((b * c) - (((b-a) * c)/2))
quadrado = (b * b)
retangulo = (a * b)
print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)


