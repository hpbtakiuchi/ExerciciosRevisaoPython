num0 = float(input("Digite um numero decimal: "))
num1 = float(input("Digite outro numero decimal: "))

soma = (f"Resultado soma: {num0 + num1}\n")

resposta = int(input("Digite a operação:\n-----------\n1-Soma\n-----------\nOperação desejada: "))

if resposta == 1:
    print("--------------\n")
    print(soma)
else: 
    print("\nOperação invalida!\n")