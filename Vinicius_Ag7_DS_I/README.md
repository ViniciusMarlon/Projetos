# 💧 Sistema de Consumo de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)
![Licença](https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge)

---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido durante a **Agenda 7** do curso Técnico em Desenvolvimento de Sistemas. O objetivo é criar um programa em Python que analise o consumo mensal de água (em m³) de um imóvel, aplicando regras de classificação baseadas no tipo de imóvel (casa, apartamento ou comercial).

O sistema utiliza **estruturas de decisão compostas** (`if`, `elif`, `else`) combinadas com **operadores lógicos** (`and`, `or`) para determinar a situação do consumo e exibir mensagens personalizadas ao usuário.

---

## 🎯 Objetivo do Sistema

- Receber o tipo de imóvel (casa, apartamento, comercial)
- Receber o consumo mensal de água em m³
- Aplicar regras de classificação de consumo
- Exibir uma mensagem informando a situação do consumo

---

## 🧮 Regras de Negócio

| Condição | Mensagem Exibida |
|:---|:---|
| Tipo = "comercial" | Tarifa comercial aplicada - consulte o plano corporativo. |
| Tipo = "apartamento" **e** consumo < 10 m³ | Consumo econômico - excelente controle de água! |
| Tipo = "apartamento" **ou** "casa" **e** consumo ≤ 25 m³ | Consumo moderado - dentro do padrão residencial. |
| Consumo ≥ 25 m³ | Consumo excessivo - adote medidas de economia e verifique vazamentos. |

---

## 🛠️ Tecnologias Utilizadas

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code" />
  <img src="https://img.shields.io/badge/Energia-FFD700?style=for-the-badge&logo=lightning&logoColor=black" alt="Energia" />
</p>

- **Linguagem:** Python 3.14
- **Ambiente:** VS Code
- **Controle de Versão:** Git e GitHub
- **Bibliotecas:** Nenhuma (apenas recursos nativos do Python)