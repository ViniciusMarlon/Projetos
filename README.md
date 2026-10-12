# 🚰 Sistema de Classificação de Nível de Reservatório

Projeto da **Agenda 11 — Bibliotecas** do curso Técnico em Desenvolvimento de Sistemas (SEAD — Governo do Estado de São Paulo).

Simula a leitura de um sensor de nível de reservatório e exibe o status com **cores diferentes** no terminal.

---

## 🎯 O que faz

- Sorteia um nível de **1 a 5** com `random`;
- Classifica em: **Muito Baixo**, **Baixo**, **Médio**, **Alto** ou **Muito Alto**;
- Exibe o status colorido com a biblioteca `colorama`.

| Nível | Status | Cor |
|-------|--------|-----|
| 1 | Muito Baixo (Crítico) | 🔴 Vermelho |
| 2 | Baixo | 🟡 Amarelo |
| 3 | Médio | 🟢 Verde |
| 4 | Alto | 🔵 Ciano |
| 5 | Muito Alto (Alerta) | 🔷 Azul |

---

## 🛠️ Tecnologias

- Python 3.x
- `random` (padrão)
- `colorama` (externa)

---

## 🚀 Como executar

```bash
# 1. Criar e ativar ambiente virtual (recomendado)
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS

# 2. Instalar dependência
pip install colorama

# 3. Rodar o programa
python app.py
```

---

## 💻 Exemplo de saída

```
Nível do reservatório: Muito Alto (Alerta)
```

A mensagem aparece **colorida** conforme o nível sorteado. Cada execução pode gerar um resultado diferente.

---

## 📄 Código principal

```python
import random
from colorama import Fore, Style

def cores_conforme(nivel):
    if nivel == 1:
        return Fore.RED, "Muito Baixo (Nível crítico)"
    elif nivel == 2:
        return Fore.YELLOW, "Baixo"
    elif nivel == 3:
        return Fore.GREEN, "Médio"
    elif nivel == 4:
        return Fore.CYAN, "Alto"
    elif nivel == 5:
        return Fore.BLUE, "Muito Alto (Alerta)"
    else:
        return Style.RESET_ALL, "Desconhecido"

nivel = random.randint(1, 5)
cor, mensagem = cores_conforme(nivel)

print(f"Nível do reservatório: {cor}{mensagem}{Style.RESET_ALL}")
```

---

## 📚 Conceitos aplicados

- Importação de bibliotecas
- Funções com `def` e `return` (múltiplos valores)
- Condicionais `if / elif / else`
- Aleatoriedade com `random`
- Cores no terminal com `colorama`
- `f-strings` para formatar saída
