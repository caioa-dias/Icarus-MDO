#=====================================================================================================================================#
#                                             CRITICAL SECTION METHOD

from solver_evaluations import avl_analysis, bidimensional_clmax

def lift_evaluation(wing, velocity, density, viscosity):
    angle_of_attack = 10
    cl_dist = avl_analysis(wing, angle_of_attack)[1]
    stall_position = cl_dist.index(max(cl_dist))
    CL = avl_analysis(wing, angle_of_attack)[2]
    CL0 = avl_analysis(wing, 0)[2]

    if stall_position != 0:
        CL = 0.1
        stall_angle = 0
    else:
        clmax_sections = bidimensional_clmax(wing, velocity, density, viscosity)[1]
        while clmax_sections[0] > cl_dist[0]:
            angle_of_attack += 0.1
            CL = avl_analysis(wing, angle_of_attack)[2]
            cl_dist = avl_analysis(wing, angle_of_attack)[1]
            stall_angle = angle_of_attack
            if angle_of_attack == 18:
                stall_angle = angle_of_attack
                break
    return(CL, CL0, stall_angle)