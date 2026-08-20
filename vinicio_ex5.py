print("Operações: 1-Soma | 2-Subtração | 3-Multiplicação | 4-Divisão")
operacao = input("Escolha a operação (1/2/3/4): ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if operacao == '1':
    print(f"Resultado: {n1 + n2}")
elif operacao == '2':
    print(f"Resultado: {n1 - n2}")
elif operacao == '3':
    print(f"Resultado: {n1 * n2}")
elif operacao == '4':
    print(f"Resultado: {n1 / n2}" if n2 != 0 else "Erro: Divisão por zero.")
else:
    print("Operação inválida.")