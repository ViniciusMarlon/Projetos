import random 
from colorama import Fore, Style

def cores_conforme(nivel):
    if nivel == 1:
        return Fore.RED, "Muito Baixo(Nivel crítico)"
    elif nivel == 2:
        return Fore.YELLOW, "Baixo"
    elif nivel == 3:
        return Fore.GREEN, "Médio"
    elif nivel == 4:
        return Fore.CYAN, "Alto"
    elif nivel == 5:
        return Fore.BLUE, "Muito Alto(Alerta)"
    else:
        return Style.RESET_ALL, ""


nivel = random.randint(1, 5)
cor, mensagem = cores_conforme(nivel)
print(f"Nível {nivel}: {cor}{mensagem}{Style.RESET_ALL}")