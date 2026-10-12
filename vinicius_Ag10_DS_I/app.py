# Função para calcular a média das notas
def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)
# Testando a função calcular_media
print(calcular_media([8, 7, 9]))   # Paulo
print(calcular_media([5, 6, 4]))   # Ana
# Calculando as médias dos alunos
media_paulo = calcular_media([8, 7, 9])
media_ana   = calcular_media([5, 6, 4])
# Função para verificar aprovação com base na média
def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
# Testando a função verificar_aprovacao
print(verificar_aprovacao(media_paulo))  # Paulo
print(verificar_aprovacao(media_ana))    # Ana
# Função para comparar o desempenho dos alunos
def desempenho(media_paulo, media_ana):
    if media_paulo > media_ana:
        return "Paulo teve melhor desempenho."
    elif media_paulo < media_ana:
        return "Ana teve melhor desempenho."
    else:
        return "Ambos tiveram o mesmo desempenho."

print(desempenho(media_paulo, media_ana))