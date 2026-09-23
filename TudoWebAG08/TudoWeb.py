excelente = 0
bom = 0
ruim = 0
i = 0
while i < 10:
    nome= input("Digite seu nome: ")
    idade= input("Digite sua idade: ")
    opiniao= input("Digite sua opinião sobre o produto (1-Excelente, 2-Bom, 3-Ruim): ")

    if opiniao == "1":
        excelente += 1
    elif opiniao == "2":
        bom += 1
    elif opiniao == "3":
        ruim += 1
    else:
        print("Opção inválida! Esta opinião não será contada.")

    i += 1


print(f"Quantidade de EXCELENTE: {excelente}")
print(f"Quantidade de BOM: {bom}")
print(f"Quantidade de RUIM: {ruim}")