<div align="center">

# ⚡ Simulação de Confiabilidade de Sistemas Elétricos
### 🔍 Estimativa de LOLP (Loss of Load Probability) via Monte Carlo

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Estável-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


---

## 📖 Sobre o Projeto
Este projeto implementa uma **simulação de confiabilidade** para sistemas elétricos usando o **método de Monte Carlo**, avaliando a probabilidade de falha do sistema (**LOLP - Loss of Load Probability**) com base em parâmetros de falhas de equipamentos.

A simulação considera falhas estocásticas em:
- Geradores
- Linhas de transmissão
- Transformadores

---

## 🚀 Funcionalidades
✔️ Cálculo de parâmetros de confiabilidade (λ, μ, p1)  
✔️ Simulação estocástica via Monte Carlo  
✔️ Critério de parada baseado em **α (erro relativo)**  
✔️ Estimativa precisa da **LOLP**  
✔️ Separação entre **módulo de funções** e **script principal**  

---

## 📂 Estrutura do Projeto
```
📁 projeto_simulacao
 ├── funcoes_sistema.py   # Módulo com funções auxiliares
 ├── main_simulacao.py    # Script principal de execução
 └── README.md            # Documentação do projeto
```

---

## ⚙️ Parâmetros Utilizados
| Componente      | Quantidade | λ (falhas/ano) | r (tempo falhado, anos) |
|-----------------|------------|-----------------|-------------------------|
| **Geradores**   | 5          | 7               | 14/8760                 |
| **Linhas**      | 17         | 2.6             | 2.8/8760                |
| **Transformadores** | 3      | 0.11            | 40/8760                 |

- Critério de parada: **α ≤ 5%**  
- Critério de falha: **4 equipamentos falhados**

---

## ▶️ Como Executar
### 1️⃣ Clone o repositório
```bash
git clone https://github.com/SEU-USUARIO/simulacao-confiabilidade.git
cd simulacao-confiabilidade
```

### 2️⃣ Execute o script principal
```bash
python main_simulacao.py
```

> 💡 **Dica:** Certifique-se de que `funcoes_sistema.py` está no mesmo diretório do script principal.

---

## 📊 Exemplo de Saída
```
================================================================================
Programa iniciado  29/07/2025 16:00:00

================================== PARÂMETROS ==================================
1) Geradores
Quantidade de componentes: 5
Falhas por ano: 7
Tempo médio em reparo (horas): 14.00
Probabilidade de estar falhado: 0.012365 %

...

================================== RESULTADOS ==================================
Cenários executados: 999999
Critério de falha: 4 equipamento(s)
Critério de parada: alfa <= 5.0 %
Valor de alfa: 4.2130 %
LOLP (prob. falha sist.): 0.001253 %

================================================================================
Programa executado em 00 h 00 min 12.35 s
================================================================================
```

---

## 📈 Melhorias Futuras
- [ ] Interface gráfica para visualização dos resultados  
- [ ] Entrada de parâmetros via linha de comando (CLI)  
- [ ] Exportação de resultados em `.csv` e gráficos de convergência  

---

## 🧑‍💻 Autor
- **Daniel dos Santos Amador**
- **Pedro Nogueira Feijó**
- **Rafael Nunes de Souza Lourenço Vieira**

📌 [GitHub](https://github.com/Daniel-sntsa)  
📧 *danields.amador@gmail.com*

---

<div align="center">

💡 *"A confiabilidade é o coração de um sistema elétrico robusto."* ⚡

</div>
