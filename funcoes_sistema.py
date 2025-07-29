from math import sqrt
import random

# =================== FUNÇÕES =================== #

def calc_parametros(lambda_, r):
    """
    Recebe lambda (taxa de falha, falhas/ano) e r (tempo médio em falha, anos)
    Retorna: m (tempo médio operando), lambda, r, mu (taxa de reparo), p1 (prob. de falha)
    """
    m = 1 / lambda_
    mu = 1 / r
    p1 = lambda_ / (lambda_ + mu)
    return (m, lambda_, r, mu, p1)

def sorteio_componente(n, p1, vetor):
    """
    Realiza sorteio do estado de n componentes.
    - 1: falhado
    - 0: funcionando
    """
    for _ in range(n):
        aleatorio = random.random()
        vetor.append(1 if aleatorio < p1 else 0)

def imprime_parametros(n, lambda_, r, p1):
    print(f"Quantidade de componentes: {n} \n"
          f"Falhas por ano: {lambda_} \n"
          f"Tempo médio em reparo (horas): {r*8760:.2f}\n"
          f"Probabilidade de estar falhado: {p1*100:.6f} %")

def imprime_resultados(n, eqs_falhos, alfa_criterio, alfa, E_falha):
    print(f"Cenários executados: {n-1} \n"
          f"Critério de falha: {eqs_falhos} equipamento(s) \n"
          f"Critério de parada: alfa <= {alfa_criterio*100} % \n"
          f"Valor de alfa: {alfa*100:.4f} % \n"
          f"LOLP (prob. falha sist.): {E_falha*100:.10f} %")

