# Entrada
valor_total=float(input("Digite o valor total da compra:"))

# Decisão do desconto
if valor_total < 200:
    desconto = 5
elif valor_total >= 200 and valor_total < 300:
    desconto = 10
else:
    desconto = 15

# Cálculo do valor final com desconto
valor_desconto = (valor_total * desconto) / 100
valor_final = valor_total - valor_desconto

# Saida
print("Você recebeu um desconto de {}%".format(desconto))
print("O valor do desconto é de R$ {:.2f}".format(valor_desconto))
print("O valor da compra com desconto é de R$ {:.2f}".format(valor_final))