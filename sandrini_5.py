
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


print("\nEscolha uma das operações básicas:")
print("+ : Adição")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")

operacao = input("Digite o símbolo da operação desejada: ")

if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operação inválida.")
