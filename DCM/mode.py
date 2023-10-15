def get_mode_parameters(mode):
    mode_parameters = [0]*25

    mode_parameters[0] = 1
    mode_parameters[1] = 1

    if mode[0] == 'A':
        mode_parameters[6] = 1
        mode_parameters[8] = 1

    if mode[0] == 'V':
        mode_parameters[7] = 1
        mode_parameters[9] = 1

    return mode_parameters

#0 = LRL, 1 = URL, 6 = AA, 7 = VA, 8 = APW, 9 = VPW, 12 = VRP, 13 = ARP
def get_parameter_details(parameter):
    # name, default, unit, lower[i], upper[i], inc[i]
    if parameter == 0:
        return ["Lower Rate Limit", 60, "ppm", 30, 50, 5, 50, 90, 1, 90, 175, 5]
    elif parameter == 1:
        return ["Upper Rate Limit", 120, "ppm", 50, 175, 5]
     # default, unit, (special), lower[i], upper[i], inc[i]
    elif parameter == 6:
        return ["Atrial Amplitude", 3.5, "V", 0, 0.5, 3.2, 0.1, 3.5, 7.0, 0.5]
    elif parameter == 7:
        return ["Ventricular Amplitude", 3.5, "V", 0, 0.5, 3.2, 0.1, 3.5, 7.0, 0.5]
    elif parameter == 8:
        return ["Atrial Pulse Width", 0.4, "ms", 0.05, 0.1, 1.9, 0.1]
    elif parameter == 9:
        return ["Ventricular Pulse Width", 0.4, "ms", 0.05, 0.1, 1.9, 0.1]
    elif parameter == 12:
        return ["VRP", 320, "ms", 150, 500, 10]
    elif parameter == 13:
        return ["ARP", 250, "ms", 150, 500, 10]