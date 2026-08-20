intervalo = [1,2,3,4,5,6,7,8,9,10]
nota = float((input("Digite sua nota da prova: ")))

if nota in intervalo:
    print(f"Nota registrada\nNota: {nota}")
else:
    print("Nota invalida!")