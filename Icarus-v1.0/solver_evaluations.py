#=====================================================================================================================================#
#                                                    WING-AIRFOIL EVALUATIONS

import os
import subprocess
import numpy as np

#=====================================================================================================================================#
#                                                  INDIVIDUAL AIRFOIL ANALYSIS

def airfoil_analysis(airfoil, Reynolds):
    # XFoil inputs setup
    airfoil_name = airfoil
    alpha_i = 9
    alpha_f = 15
    alpha_step = 0.1
    Re = Reynolds
    n_iter = 100

    # XFoil analysis
    if os.path.exists("2d_output.txt"):
        os.remove("2d_output.txt")
    input_file = open("2d_input.in", 'w')
    input_file.write("LOAD {0}.dat \n".format(airfoil_name)) 
    input_file.write("OPER \n")
    input_file.write("Visc {0}\n".format(Re))
    input_file.write("ITER {0}\n".format(n_iter))
    input_file.write("PACC \n")
    input_file.write("2d_output.txt\n\n")
    input_file.write("as {0} {1} {2}\n".format(alpha_i, alpha_f, alpha_step))
    input_file.write("PACC\n\n")
    input_file.write("quit \n")
    input_file.close()
    subprocess.call("xfoil.exe < 2d_input.in", shell=True)

    # Polar data analysis to obtain Cl_max and Alpha_stall
    polar_data = (np.loadtxt("2d_output.txt", skiprows=12)).T
    alpha = polar_data[0]
    cl = polar_data[1]

    clmax = 0
    step = -1
    for i in cl:
        if i > clmax:
            clmax = i
            step+=1
        else:
            break

    # To get the alpha stall for each airfoil, put alpha[step] on the return
    return(clmax)



#-------------------------------------------------------------------------------------------------------------------------------------#
#                                               AIRFOIL ANALYSIS ACROSS THE SPAN


def bidimensional_clmax(wing, velocity, density, viscosity):
    chord_root = wing[0]
    chord_tip = wing[1]
    straight_span = wing[2]
    trapezoidal_span = wing[3]
    span = straight_span + trapezoidal_span
    airfoil = wing[6]
    
    # Chord calculation for different sections across the span
    def chord_calculation(s):
        if s <= straight_span:
            chord = chord_root
        if s > straight_span:
            s = s - straight_span
            delta_chord = (s*(chord_root - chord_tip))/trapezoidal_span
            chord = chord_root - delta_chord
        return chord

    # List of span position values that will be analyzed
    span_sections = list(range(21))
    cut_point = span/20
    for i in span_sections:
        span_sections[i] = cut_point*i

    # List of chord values that will be analyzed
    chord_sections = list(range(21))
    for i in range(len(span_sections)):
        chord_sections[i] = chord_calculation(span_sections[i])

    # List of Reynolds Number values that will be analyzed
    reynolds_sections = list(range(21))
    for i in range(len(chord_sections)):
        reynolds_sections[i] = ((chord_sections[i]*velocity*density)/viscosity)

    # List of Cl_max values for each span section
    clmax_sections = list(range(21))
    for i in range(len(span_sections)):
        if reynolds_sections[i-1] == reynolds_sections[i]:
            clmax_sections[i] = clmax_sections[i-1]
        else:
            clmax_sections[i] = airfoil_analysis(airfoil, reynolds_sections[i])

    return(span_sections, clmax_sections)



#-------------------------------------------------------------------------------------------------------------------------------------#
#                                                    WING ANALYSIS

def avl_analysis(wing, angle_of_attack):
    # Inputs organization for the AVL file run
    chord_root = wing[0]
    chord_tip = wing[1]
    straight_span = wing[2]
    trapezoidal_span = wing[3]
    offset_mid = wing[4]
    offset_tip = wing[5]
    airfoil = wing[6]
    wing_area = (chord_root*straight_span) + (((chord_root+chord_tip)*trapezoidal_span)/2)
    mean_aerodynamic_chord = ((2/3)*chord_root*((1 + 1 + (1)**2)/(1 + 1))*(chord_root*straight_span) + (2/3)*chord_root*((1 + (chord_tip/chord_root) + 
            (chord_tip/chord_root)**2)/(1 + (chord_tip/chord_root)))*(((chord_root+chord_tip)*trapezoidal_span)/2))/((chord_root*straight_span) + 
            (((chord_root+chord_tip)*trapezoidal_span)/2))
    x_mean_aerodynamic_chord = xmacw = (((((offset_mid)/2)*(chord_root*straight_span)) + (offset_mid + (offset_tip - offset_mid)*(1 + 2*(chord_tip/chord_root))/(3 + 3*(chord_tip/chord_root))
             * (((chord_root+chord_tip)*trapezoidal_span)/2)))/((chord_root*straight_span) + 
            (((chord_root+chord_tip)*trapezoidal_span)/2)))

    # Input file creation
    if os.path.exists("3d_input.avl"):
        os.remove("3d_input.avl")
    geometry_file = ''' 
    Zeus
0.0                                 | Mach
0     0     0.0                     | iYsym  iZsym  Zsym
{}     {}     {}   | Sref   Cref   Bref
{}     0.00000     0.00000   | Xref   Yref   Zref

#==============================================================
SURFACE
wing
# Horseshoe Vortex Distribution
10     1.0     20     1.0    |  Nchord  Cspace  Nspan  Sspace

# Reflect image wing about y=0 plane
YDUPLICATE
0.0

# Twist angle bias for whole surface
ANGLE
0.0


# Here the sections start
#---INNER SECTION-------------------------------------------------
#  Xle      Yle       Zle       Chord     angle
SECTION
0.0000    0.0000    0.0000    {}   0.000

AFIL 0.0 1.0
{}.dat

#---SECTION 2------------------------------------------------------
#  Xle      Yle       Zle       Chord     angle
SECTION
{}    {}    0.0000   {}   0.000

AFIL 0.0 1.0
{}.dat

#---END SECTION---------------------------------------------------
#  Xle      Yle       Zle       Chord     angle
SECTION
{}    {}    0.0000    {}   0.000

AFIL 0.0 1.0
{}.dat

# Created by Caio Dias 09.02.2024
'''.format(wing_area*2,
        mean_aerodynamic_chord,
        ((straight_span + trapezoidal_span)*2),
        x_mean_aerodynamic_chord + ((1/4)*mean_aerodynamic_chord),
        chord_root,
        airfoil,
        offset_mid,
        straight_span,
        chord_root,
        airfoil,
        offset_tip,
        (straight_span + trapezoidal_span),
        chord_tip,
        airfoil)


    # AVL analysis
    file_name = "3d_input.avl"

    with open(file_name, 'w') as archive:
        archive.write(geometry_file)

    input_avl_file = open("3d_input.in", 'w')
    input_avl_file.write("LOAD {0} \n".format(file_name))
    input_avl_file.write("OPER \n")
    input_avl_file.write("a \n")
    input_avl_file.write("a {0} \n".format(angle_of_attack))
    input_avl_file.write("xx \n")
    input_avl_file.write("FS \n")
    input_avl_file.write("3d_output.txt \n")
    input_avl_file.write("O \n")
    input_avl_file.write("quit \n")
    input_avl_file.close()

    subprocess.call("avl.exe < 3d_input.in", shell=True)

    with open("3d_output.txt", 'r') as archive:
        file = np.loadtxt(archive.readlines()[20:40]).T

    with open("3d_output.txt", 'r') as archive:
        cl_wing_file = archive.readlines()[9]
        CL = 2*(float(cl_wing_file[17:24]))   

    # Polar data analysis to obtain Cl Distribution and Span Points
    span_point = []
    cl_dist = []
    for i in range(20):
        span_point.append((file[1])[i])
        cl_dist.append((file[7])[i])

    return(span_point, cl_dist, CL)