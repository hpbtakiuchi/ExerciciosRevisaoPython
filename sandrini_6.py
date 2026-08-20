
print("Este programa calcula o fatorial de um número inteiro não negativo.")
numero = int(input("Por favor, digite um número inteiro: "))

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")
