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

def T1(v):
    return -0.0427*(v**2) - 0.2933*v + 59.18
def T2(v):
    return -0.0340*(v**2) - 0.2335*v + 64.452
def T3(v):
    return -0.0279*(v**2) - 0.1915*v + 62.86

velocity = 18
density = 1.117
viscosity = 0.0000184
wing = [0.45058, 0.27567, 0.5205455692589661, 1.6-0.5205455692589661, 0, 0.021785738462550164, 'UruA10412', T2] 
# chord_root, chord_tip, straight_span, trapezoidal_span, offset_mid, offset_tip, airfoil, thrust

h_obs = 0.85 # 0.1m more than the real obstacle
S_max = 55 #m

print(MTOW(wing, S_max, h_obs, density, velocity, viscosity))