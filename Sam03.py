import math

raio = float(input("Digite o raio da circunferência: "))
diametro = 2 * raio
area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio

print(f"Diâmetro: {diametro:.2f}")
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
