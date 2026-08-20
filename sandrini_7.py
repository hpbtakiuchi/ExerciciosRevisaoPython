n = int(input("Digite a quantidade n de números de Fibonacci: "))

if n <= 0:
    print("Por favor, digite um número maior que zero.")
else:
    soma = 0
    a, b = 0, 1
    
  
    for _ in range(n):
        soma += a
        a, b = b, a + b  
        
    print(f"A soma dos {n} primeiros números da sequência de Fibonacci é: {soma}")
