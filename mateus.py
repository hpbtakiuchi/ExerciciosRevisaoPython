print("olá, professor")

while True:
    entrada = input("digite os números a serem somados : ").split()
    if (len(entrada) > 2):
        print("Apenas 2 números")
        break
    
    operacao = input("digite o operador matemático : ")

    if (len(entrada) > 2):
        print("Apenas 2 números")

    tratamentoOne =float(entrada[0])
    tratamentoTwo =float(entrada[1])

    if (operacao == "+") :
        print(tratamentoOne + tratamentoTwo)

    elif (operacao == "-") :
        print(tratamentoOne - tratamentoTwo)

    elif (operacao == "/") :
        print(tratamentoOne / tratamentoTwo)

    elif (operacao == "*") :
        print(tratamentoOne * tratamentoTwo)

    else :
        print("Error")