#AJEITAR O VALOR DE CDCL E CLAF
#CONSIDERAR USAR O CDI DIRETO DO AVL
#FAZER ANÁLISE DE CONVERGÊNCIA PARA O ARQUIVO DE DISCRETIZAÇÃO
#ADICIONAR MAIS PERFIS PARA EH
#corda entre 50 e 60 cm
#envergadura entre 3 e 3.5 m
# parte reta de no mínimo 50 cm em meia asa - longarina

# FAZER A ANÁLISE DE ESTABILIDADE

# restrição de longarina ser reta
# análise de pouso
# restringir envergadura reta
# MTOW DO ITA NO EAST = 16.5 KG
# LIMITAR A DISTÂNCIA DO EH EM ATÉ 0.8 m

from performance_analysis import MTOW


velocity = 15
density = 1.1104
viscosity = 0.0000184
wing = [0.5, 0.28, 0.55, 1.05, 0, 0.06, 'E423'] # chord_root, chord_tip, straight_span, trapezoidal_span, offset_mid, offset_tip, airfoil

def curva_tracao(v):
    return -0.031*(v**2) - 0.213*v + 69.903

h_obs = 0.8 # 0.1m more than the real obstacle
S_max = 55 #m

print(MTOW(wing, curva_tracao, S_max, h_obs, density, velocity, viscosity))