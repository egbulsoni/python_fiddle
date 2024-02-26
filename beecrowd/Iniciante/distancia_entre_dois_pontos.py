import math
p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))
x1 = p1[0]
y1 = p1[1]
x2 = p2[0]
y2 = p2[1]

distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
print("%.4f" % distancia)