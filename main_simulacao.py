import time
import random
from funcoes_sistema import *

# =================== CONFIGURAÇÕES INICIAIS =================== #

random.seed(1513)
inicio = time.perf_counter()
print(f"\n{'='*80}\n")
print("Programa iniciado", time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))

# =================== DADOS DO SISTEMA =================== #

alfa_maximo = 0.05   # critério de parada sendo o alfa
eqs_falhos = 4       # quantidade de equipamentos falhados

# Geradores
n_g, lambda_g, r_g = 5, 7, 14/8760
# Linhas
n_l, lambda_l, r_l = 17, 2.6, 2.8/8760
# Trafos
n_t, lambda_t, r_t = 3, 1.1E-01, 40/8760

# =================== CÁLCULO DOS PARÂMETROS =================== #

m_g, lambda_g, r_g, mu_g, p1_g = calc_parametros(lambda_g, r_g)
m_l, lambda_l, r_l, mu_l, p1_l = calc_parametros(lambda_l, r_l)
m_t, lambda_t, r_t, mu_t, p1_t = calc_parametros(lambda_t, r_t)

# =================== SIMULAÇÃO MONTE CARLO =================== #

falhas, n, alfa = 0, 1, 1
numerador, E_falha, iterador = 0, 0, 1

while alfa > alfa_maximo:
    vetor = []
    sorteio_componente(n_g, p1_g, vetor)
    sorteio_componente(n_l, p1_l, vetor)
    sorteio_componente(n_t, p1_t, vetor)

    if sum(vetor) >= eqs_falhos:
        falhas += 1
        x_novo = 1
    else:
        x_novo = 0

    E_falha = falhas / n
    numerador += (x_novo - E_falha) ** 2
    variancia = numerador / (n ** 2)

    if E_falha != 0 and variancia != 0:
        alfa = sqrt(variancia) / E_falha

    n += 1
    if (n-1) == (1e09 * iterador):
        print(f"Cenários atual: {n-1} \nAlfa atual: {alfa*100:.4f} % \n"
              f"LOLP atual prob. falha sist.: {E_falha*100:.10f} %")
        iterador += 1

# =================== RESULTADOS =================== #

print(f'\n{"="*34} PARÂMETROS {"="*34}\n')
print("1) Geradores\n")
imprime_parametros(n_g, lambda_g, r_g, p1_g)
print("\n2) Linhas\n")
imprime_parametros(n_l, lambda_l, r_l, p1_l)
print("\n3) Trafos\n")
imprime_parametros(n_t, lambda_t, r_t, p1_t)

print(f'\n{"="*34} RESULTADOS {"="*34}\n')
imprime_resultados(n, eqs_falhos, alfa_maximo, alfa, E_falha)

print(f"\n{'='*80}\n")

# =================== TEMPO DE EXECUÇÃO =================== #

fim = time.perf_counter()
duracao = fim - inicio
h, resto = divmod(duracao, 3600)
m, s = divmod(resto, 60)
print(f"Programa executado em {int(h):02d} h {int(m):02d} min {s:05.2f} s")
print(f"\n{'='*80}\n")
