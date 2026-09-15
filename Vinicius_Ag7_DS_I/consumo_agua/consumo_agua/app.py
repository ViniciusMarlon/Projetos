tipo_imovel= input("Digite o tipo de imóvel (casa, apartamento,comercial): ")
consumo_mensal_m3= float(input("Digite o consumo mensal em m³: "))

if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipo_imovel == "apartamento" and consumo_mensal_m3 < 10:
    print("Consumo econômico – excelente controle de água!")
elif tipo_imovel == "apartamento" or "casa" and consumo_mensal_m3 <= 25:
    print("Consumo moderado – dentro do padrão residencial.")
elif consumo_mensal_m3 >= 25:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

