INPUT.world.gravity = 9.81;  %(m/s²)
INPUT.world.density = 1.108; %(kg/m³)
INPUT.world.friction = 0.04;
INPUT.decisions.TO_dist = 55; %(m)
INPUT.decisions.obstacle = 0.8; %(m)
INPUT.decisions.friction_drag = 0.016;
INPUT.decisions.wing_density = 1.5;

GENETIC_PARAMETERS.cons = [0.200 0.500    % Corda na Raíz (m)
                           0.200 1.000    % Razão de Afilamento (%)
                           2.000 3.600    % Envergadura (m)
                           0.200 1.000    % Posição de Afilamento (%)
                           0.000 0.080    % Offset na Ponta
                           0.000 1.000    % Torção Intermediária (cat)
                           0.000 1.000    % Torção na Ponta (cat)
                           0.000 1.000    % Aerofólio (cat)                           
                           0.000 1.000];  % Grupo Motopropulsor (cat)

GENETIC_PARAMETERS.max_generations = 120;
GENETIC_PARAMETERS.pop_size = 40;
GENETIC_PARAMETERS.prob_crossover = 0.85;
GENETIC_PARAMETERS.prob_mutation = 0.15;
GENETIC_PARAMETERS.elitism_preservation = 2;

[GENETIC_OUTPUTS] = GA_ELITISM(INPUT, GENETIC_PARAMETERS);