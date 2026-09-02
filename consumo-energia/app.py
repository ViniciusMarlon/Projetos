#Entrada de dados
aparelho= input("Digite o nome do aparelho: ")
potencia= float(input("Digite a potencia do aparelho (Watts):"))
tpm= float(input("Digite o tempo médio de uso diario em horas:"))        
#Processamento - consumo
consumomensal= (potencia * tpm * 30) /1000
#Processamento - custo
kwh= 0.75
custo_estimado= consumomensal * kwh
#Saida de dados
print("O consumo mensal do aparelho", aparelho,"é de", consumomensal, "kWh.")
print(f"O aparelho {aparelho} custa aproximadamente R$ {custo_estimado:.2f} por mês em energia.")