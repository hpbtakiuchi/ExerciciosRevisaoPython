import math

raio = float(input("Digite o valor do raio da circunferência: "))

diametro = 2 * raio
area = math.pi * (raio ** 2)
perimetro = 2 * math.pi * raio

print(f"Diâmetro: {diametro:.2f}")
print(f"Área do círculo: {area:.2f}")
print(f"Perímetro do círculo: {perimetro:.2f}")
