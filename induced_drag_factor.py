def induced_drag(aspect_ratio, taper_ratio):
    if taper_ratio <= 0.025:
        induced_drag_factor = -0.0005*(aspect_ratio**2) + 0.0185*aspect_ratio - 0.003
    if 0.025 < taper_ratio <= 0.05:
        induced_drag_factor = -0.0004*(aspect_ratio**2) + 0.015*aspect_ratio - 0.0051
    if 0.05 < taper_ratio <= 0.075:
        induced_drag_factor = -0.0003*(aspect_ratio**2) + 0.0121*aspect_ratio - 0.0066
    if 0.075 < taper_ratio <= 0.1:
        induced_drag_factor = -0.0002*(aspect_ratio**2) + 0.0098*aspect_ratio - 0.0067
    if 0.1 < taper_ratio <= 0.125:
        induced_drag_factor = -0.0002*(aspect_ratio**2) + 0.0079*aspect_ratio - 0.0064
    if 0.125 < taper_ratio <= 0.15:
        induced_drag_factor = -0.0001*(aspect_ratio**2) + 0.0065*aspect_ratio - 0.0059
    if 0.15 < taper_ratio <= 0.2:
        induced_drag_factor = -0.00008*(aspect_ratio**2) + 0.0044*aspect_ratio - 0.0048
    if 0.2 < taper_ratio <= 0.25:
        induced_drag_factor = -0.00004*(aspect_ratio**2) + 0.0031*aspect_ratio - 0.0039
    if 0.25 < taper_ratio <= 0.3:
        induced_drag_factor = -0.00002*(aspect_ratio**2) + 0.0024*aspect_ratio - 0.0035
    if 0.3 < taper_ratio <= 0.35:
        induced_drag_factor = -0.000007*(aspect_ratio**2) + 0.0021*aspect_ratio - 0.0034
    if 0.35 < taper_ratio <= 0.4:
        induced_drag_factor = -0.0000008*(aspect_ratio**2) + 0.0021*aspect_ratio - 0.0035
    if 0.4 < taper_ratio <= 0.45:
        induced_drag_factor = 0.0000007*(aspect_ratio**2) + 0.0023*aspect_ratio - 0.0039
    if 0.45 < taper_ratio <= 0.5:
        induced_drag_factor = -0.000001*(aspect_ratio**2) + 0.0027*aspect_ratio - 0.0045
    if 0.5 < taper_ratio <= 0.6:
        induced_drag_factor = -0.00001*(aspect_ratio**2) + 0.004*aspect_ratio - 0.0061
    if 0.6 < taper_ratio <= 0.7:
        induced_drag_factor = -0.00003*(aspect_ratio**2) + 0.0055*aspect_ratio - 0.0081
    if 0.7 < taper_ratio <= 0.8:
        induced_drag_factor = -0.00006*(aspect_ratio**2) + 0.0073*aspect_ratio - 0.0103
    if 0.8 < taper_ratio <= 0.9:
        induced_drag_factor = -0.00009*(aspect_ratio**2) + 0.0093*aspect_ratio - 0.0125
    if 0.9 < taper_ratio <= 1:
        induced_drag_factor = -0.0001*(aspect_ratio**2) + 0.0113*aspect_ratio - 0.0148
    
    k_cdi = (1 + induced_drag_factor)/(3.14159*aspect_ratio)

    return (k_cdi)