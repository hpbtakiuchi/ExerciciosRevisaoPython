
lista_clientes = []

while True:
    
    print("\n--- Sistema de Clientes ---")
    print("a) Inserir Dados")
    print("b) Imprimir Dados")
    print("c) Sair")
    
    opcao = input("Escolha uma opção: ").lower() # Transforma em minúsculo para facilitar a validação
    
    if opcao == 'a':
        
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        
        
        cliente = {"nome": nome, "email": email}
        lista_clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")
        
    elif opcao == 'b':
        
        if len(lista_clientes) == 0:
            print("Nenhum cliente cadastrado ainda.")
        else:
            print("\n--- Lista de Clientes Cadastrados ---")
            for i, cliente in enumerate(lista_clientes, 1):
                print(f"Cliente {i}: Nome: {cliente['nome']} | E-mail: {cliente['email']}")
                
    elif opcao == 'c':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
