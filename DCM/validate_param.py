from tkinter import messagebox

# Validate the parameters
def is_valid_parameters(updated_values, mode):
    print(updated_values)
    error_message = ""

    # Access values by their keys
    LRL = validate_lrl(updated_values['Lower Rate Limit'])
    if LRL != False:
            error_message += LRL

    URL = validate_url(updated_values['Upper Rate Limit'])
    if URL != False:
            error_message += URL

    if mode == "AOO":
        AA = validate_pa(updated_values['Atrial Amplitude'])
        if AA != False:
            error_message += AA

        APW = validate_pw(updated_values['Atrial Pulse Width'])
        if APW != False:
            error_message += APW
        
    if mode == "VOO":
        VA = validate_pa(updated_values['Ventricular Amplitude'])
        if VA != False:
            error_message += VA

        VPW = validate_pw(updated_values['Ventricular Pulse Width'])
        if VPW != False:
            error_message += VPW

    if mode == "AAI":
        AA = validate_pa(updated_values['Atrial Amplitude'])
        if AA != False:
            error_message += AA

        APW = validate_pw(updated_values['Atrial Pulse Width'])
        if APW != False:
            error_message += APW

        AS = validate_sen(updated_values['Atrial Sensitivity'])
        if AS != False:
            error_message += AS

        ARP = validate_rp(updated_values['ARP'])
        if ARP != False:
            error_message += ARP

        PVARP = validate_pvarp(updated_values['PVARP'])
        if PVARP != False:
            error_message += PVARP
        
    if mode == "VVI":
        VA = validate_pa(updated_values['Ventricular Amplitude'])
        if VA != False:
            error_message += VA

        VPW = validate_pw(updated_values['Ventricular Pulse Width'])
        if VPW != False:
            error_message += VPW

        VS = validate_sen(updated_values['Ventricular Sensitivity'])
        if VS != False:
            error_message += VS

        VRP = validate_rp(updated_values['VRP'])
        if VRP != False:
            error_message += VRP

    if error_message != "":
        messagebox.showerror("Error", error_message)
        return False
    else:
        messagebox.showinfo("Success", "Parameters Updated.")
        return True

# Validate the LRL value entered by the user
def validate_lrl(value):
    try:
        val = float(value)
    except ValueError:
        return "LRL must be a number.\n"
    
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
    try:
        val = float(value)
    except ValueError:
        return "URL must be a number.\n"
    
    if (val < 50) or (val > 175):
        return "URL must be between 50ppm and 175ppm.\n"
    elif (50 <= val) and (val <= 175) and (val % 5 != 0):
        return "URL must be a multiple of 5 between 50ppm and 175ppm.\n"
    else:
        return False

# Validate the Pulse Amplitude value entered by the user
def validate_pa(value):
    try:
        val = float(value)*100
    except ValueError:
        return "Pulse Amplitude must be a number.\n"
    
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
    try:
        val = float(value)*100
    except ValueError:
        return "Pulse Width must be a number.\n"
    
    if not ((val == 5) or ((val >= 10) and (val <= 190))):
        return "Pulse Width must be 0.05ms or between 0.1ms and 1.9ms.\n"
    elif (10 <= val) and (val <= 190) and (val % 10 != 0):
        return "Pulse Width must be a multiple of 0.1ms between 0.1ms and 1.9ms.\n"
    else:
        return False
    
# Validate the Refractory Period value entered by the user
def validate_rp(value):
    try:
        val = float(value)
    except ValueError:
        return "Refractory Period must be a number.\n"
    
    if (val < 150) or (val > 500):
        return "Refractory Period must be between 150ms and 500ms.\n"
    elif (val % 10 != 0):
        return "Refractory Period must be a multiple of 10ms between 150ms and 500ms.\n"
    else:
        return False
    
# Validate the PVARP value entered by the user
def validate_pvarp(value):
    try:
        val = float(value)
    except ValueError:
        return "PVARP must be a number.\n"
    
    if (val < 150) or (val > 500):
        return "PVARP must be between 150ms and 500ms.\n"
    elif (val % 10 != 0):
        return "PVARP must be a multiple of 10ms between 150ms and 500ms.\n"
    else:
        return False
    
# Validate the Sensitivity value entered by the user
def validate_sen(value):
    try:
        val = float(value)*1000
    except ValueError:
        return "Sensitivity must be a number.\n"
    
    if ((val == 250) or (val == 500) or (val == 750)):
        return False
    elif (val < 1000) or (val > 10000):
        return "Atrial Sensitivity must be 0.25mV, 0.5mV or 0.75mV or must be between 1.0mV and 10mV\n"
    elif (val % 500 != 0):
        return "Atrial Sensitivity must be a multiple of 0.5mV between 1.0mV and 10mV.\n"
    else:
        return False