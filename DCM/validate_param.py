# Validate the LRL value entered by the user
def validate_lrl(value):
    val = float(value)
    if (30 <= val) and (val <= 50) and (val % 5 != 0):
        return "LRL must be a multiple of 5 between 30ppm and 50ppm.\n"
    elif (50 < val) and (val <= 90) and (val % 1 != 0):
        return "LRL must be a multiple of 1 between 50ppm and 90ppm.\n"
    elif (90 < val) and (val <= 175) and (val % 5 != 0):
        return "LRL must be a multiple of 5 between 90ppm and 175ppm.\n"
    elif (val < 30) or (val > 175):
        return "LRL must be between 30ppm and 175ppm.\n"
    else:
        return False

# Validate the URL value entered by the user
def validate_url(value):
    val = float(value)
    if (val < 50) or (val > 175):
        return "URL must be between 50ppm and 175ppm.\n"
    elif (50 <= val) and (val <= 175) and (val % 5 != 0):
        return "URL must be a multiple of 5 between 50ppm and 175ppm.\n"
    else:
        return False

# Validate the Pulse Amplitude value entered by the user
def validate_pa(value):
    val = float(value)*100
    if not ((val == 0) or ((val >= 50) and (val <= 320)) or ((val >= 350) and (val <= 700))):
        return "Pulse Amplitude must be 0V, 0.5-3.2V or 3.5-7V.\n"
    elif (50 <= val) and (val <= 320) and (val % 10 != 0):
        return "Pulse Amplitude must be a multiple of 0.1V between 0.5V and 3.2V.\n" 
    elif (350 < val) and (val <= 700) and (val % 50 != 0):
        return "Pulse Amplitude must be a multiple of 0.5V between 3.5V and 7.0V.\n"
    else:
        return False

# Validate the Pulse Width value entered by the user
def validate_pw(value):
    val = float(value)*100
    if not ((val == 5) or ((val >= 10) and (val <= 190))):
        return "Pulse Width must be 0.05ms or between 0.1ms and 1.9ms.\n"
    elif (10 <= val) and (val <= 190) and (val % 10 != 0):
        return "Pulse Width must be a multiple of 0.1ms between 0.1ms and 1.9ms.\n"
    else:
        return False
    
# Validate the Refractory Period value entered by the user
def validate_rp(value):
    val = float(value)
    if (val < 150) or (val > 500):
        return "Refractory Period must be between 150ms and 500ms.\n"
    elif (val % 10 != 0):
        return "Refractory Period must be a multiple of 10ms between 150ms and 500ms.\n"
    else:
        return False