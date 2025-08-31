from lift_evaluation import lift_evaluation
from induced_drag_factor import induced_drag
import numpy as np

def MTOW (wing, S_max, h_obs, density, velocity, viscosity):
    # GEOMETRIC VALUES:
    tracao_dinamica = wing[7]
    S_ref = ((wing[0]*wing[2]) + (((wing[0]+wing[1])*wing[3])/2))*2
    empty_mass = S_ref * 1.5
    aspect_ratio = (((wing[2]+wing[3])*2)**2)/S_ref
    taper_ratio = wing[1]/wing[0]

    # AERODYNAMIC ANALYSIS:
    results = lift_evaluation(wing, velocity, density, viscosity)
    cl_max = results[0]
    cl_zero = results[1]
    k_cdi = induced_drag(aspect_ratio, taper_ratio)
    
    def takeoff_distance (mass):
        W = mass*9.81

        v_stall = (((2*W)/(density*cl_max*S_ref))**(1/2))
        v_r = 1.1 *v_stall
        v_to = v_r/(2**(1/2))

        Lift = (1/2)*density*((v_to)**2)*S_ref*cl_zero
        Drag = (1/2)*density*((v_to)**2)*S_ref*(0.02 + (cl_zero**2 * k_cdi))

        S_g = ((v_r**2)*W)/((2*9.81)*(tracao_dinamica(v_to) - Drag - 0.05*(W-Lift)))

        transition_radius = 0.2156 * (v_stall**2)

        # Horizontal distance needed to clear the obstacle
        S_obst = (transition_radius**2 - (transition_radius - h_obs)**2)**(1/2)

        # Total distance needed to lift_off and clear the obstacle
        S_to = S_g + S_obst
        return (S_to)

    mass = 10
    while takeoff_distance(mass) <= S_max:
        mass += 0.1
    if takeoff_distance(mass) > S_max:
        mass -= 0.1

    return (mass, takeoff_distance(mass), empty_mass, S_ref)
