def validate_lrl(value):
    error = ""
    val = float(value)
    if 30 <= val <= 50 and val % 5 != 0:
        return "LRL must be a multiple of 5 between 30ppm and 50ppm.\n"
    elif 50 < val <= 90 and val % 1 != 0:
        return "LRL must be a multiple of 1 between 50ppm and 90ppm.\n"
    elif 90 < val <= 175 and val % 5 != 0:
        return "LRL must be a multiple of 5 between 90ppm and 175ppm.\n"
    elif val < 30 or val > 175:
        return "LRL must be between 30ppm and 175ppm.\n"
    else:
        return False

def validate_url(value):
    error = ""
    val = float(value)
    if 50 <= val <= 175 and val % 5 != 0:
        return "URL must be a multiple of 5 between 50ppm and 175ppm.\n"
    else:
        return False

def validate_pa(value):
    error = ""
    val = float(value)
    if val < 0 or val > 7 or 3.2 < val < 3.5:
        return "Pulse Amplitude must be 0V, 0.5-3.2V or 3.5-7V.\n"
    elif 0.5 <= val <= 3.2 and val % 0.1 != 0:
        return "Pulse Amplitude must be a multiple of 0.1V between 0.5V and 3.2V.\n" 
    elif 3.5 < val <= 7.0 and val % 0.5 != 0:
        return "Pulse Amplitude must be a multiple of 0.5V between 3.5V and 7.0V.\n"
    else:
        return False

def validate_pw(value):
    error = ""
    val = float(value)
    print(val)
    print(((val*10) % 0.1))

    if 0.05 > val or val > 1.9:
        return "Pulse Width must be between 0.05ms and 1.9ms.\n"
    elif ((val*10) % 0.1) != 0:
        return "Pulse Width must be a multiple of 0.1ms between 0.1ms and 1.9ms.\n"
    else:
        return False
    
def validate_rp(value):
    error = ""
    val = float(value)
    if val < 150 or val > 500:
        return "Refractory Period must be between 150ms and 500ms.\n"
    elif val % 10 != 0:
        return "Refractory Period must be a multiple of 10ms between 150ms and 500ms.\n"
    else:
        return False