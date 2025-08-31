from lift_evaluation import lift_evaluation
from induced_drag_factor import induced_drag

def MTOW (wing, tracao_dinamica, S_max, h_obs, density, velocity, viscosity):
    # GEOMETRIC VALUES:
    S_ref = ((wing[0]*wing[2]) + (((wing[0]+wing[1])*wing[3])/2))*2
    empty_mass = S_ref
    aspect_ratio = (((wing[2]+wing[3])*2)**2)/S_ref
    taper_ratio = wing[1]/wing[0]

    # AERODYNAMIC ANALYSIS:
    results = lift_evaluation(wing, velocity, density, viscosity)
    cl_max = results[0]
    cl_zero = results[1]
    alpha_stall = results[2]
    k_cdi = induced_drag(aspect_ratio, taper_ratio)
    
    def takeoff_distance (mass):
        W = mass*9.81

        v_stall = (((2*W)/(density*cl_max*S_ref))**(1/2))
        v_lo = 1.1 *v_stall

        Lift = (1.21/2)*W*(cl_zero/cl_max)
        Drag = (1.21/2)*W* ((k_cdi*((cl_zero)**2))/cl_max)

        S_lo = ((v_lo**2)*W)/((2*9.81)* (tracao_dinamica(v_lo/((2)**(1/2)))-Drag-0.33*(W-Lift)))

        transition_radius = 0.2156 * (v_stall**2)

        # Horizontal distance needed to clear the obstacle
        S_obs = (transition_radius**2 - (transition_radius - h_obs)**2)**(1/2)

        # Total distance needed to lift_off and clear the obstacle
        S_to = S_lo + S_obs
        return (S_to)

    mass = 10
    while takeoff_distance(mass) <= S_max:
        mass += 0.1
    if takeoff_distance(mass) > S_max:
        mass -= 0.1

    return (mass, takeoff_distance(mass), empty_mass, cl_max, cl_zero, alpha_stall)