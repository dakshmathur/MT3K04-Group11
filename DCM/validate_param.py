from tkinter import messagebox

# Validate the parameters
def is_valid_parameters(updated_values, mode):
    error_message = ""

    # Access values by their keys
    LRL = validate_lrl(updated_values['LOWER RATE LIMIT'])
    if LRL != False:
            error_message += LRL

    URL = validate_url(updated_values['UPPER RATE LIMIT'])
    if URL != False:
            error_message += URL

    if mode == "AAT":
        AA = validate_pa(updated_values['ATRIAL AMPLITUDE'])
        if AA != False:
            error_message += AA

        APW = validate_pw(updated_values['ATRIAL PULSE WIDTH'])
        if APW != False:
            error_message += APW

        AS = validate_sen(updated_values['ATRIAL SENSITIVITY'])
        if AS != False:
            error_message += AS

        ARP = validate_rp(updated_values['ARP'])
        if ARP != False:
            error_message += ARP

        PVARP = validate_pvarp(updated_values['PVARP'])
        if PVARP != False:
            error_message += PVARP

    if mode == "VVT":
        VA = validate_pa(updated_values['VENTRICULAR AMPLITUDE'])
        if VA != False:
            error_message += VA

        VPW = validate_pw(updated_values['VENTRICULAR PULSE WIDTH'])
        if VPW != False:
            error_message += VPW

        VS = validate_sen(updated_values['VENTRICULAR SENSITIVITY'])
        if VS != False:
            error_message += VS

        VRP = validate_rp(updated_values['VRP'])
        if VRP != False:
            error_message += VRP

    if mode == "AOO":
        AA = validate_pa(updated_values['ATRIAL AMPLITUDE'])
        if AA != False:
            error_message += AA

        APW = validate_pw(updated_values['ATRIAL PULSE WIDTH'])
        if APW != False:
            error_message += APW
        
    if mode == "VOO":
        VA = validate_pa(updated_values['VENTRICULAR AMPLITUDE'])
        if VA != False:
            error_message += VA

        VPW = validate_pw(updated_values['VENTRICULAR PULSE WIDTH'])
        if VPW != False:
            error_message += VPW

    if mode == "AAI":
        AA = validate_pa(updated_values['ATRIAL AMPLITUDE'])
        if AA != False:
            error_message += AA

        APW = validate_pw(updated_values['ATRIAL PULSE WIDTH'])
        if APW != False:
            error_message += APW

        AS = validate_sen(updated_values['ATRIAL SENSITIVITY'])
        if AS != False:
            error_message += AS

        ARP = validate_rp(updated_values['ARP'])
        if ARP != False:
            error_message += ARP

        PVARP = validate_pvarp(updated_values['PVARP'])
        if PVARP != False:
            error_message += PVARP

        HYS = validate_hys(updated_values['HYSTERESIS'])
        if HYS != False:
            error_message += HYS
        
    if mode == "VVI":
        VA = validate_pa(updated_values['VENTRICULAR AMPLITUDE'])
        if VA != False:
            error_message += VA

        VPW = validate_pw(updated_values['VENTRICULAR PULSE WIDTH'])
        if VPW != False:
            error_message += VPW

        VS = validate_sen(updated_values['VENTRICULAR SENSITIVITY'])
        if VS != False:
            error_message += VS

        VRP = validate_rp(updated_values['VRP'])
        if VRP != False:
            error_message += VRP

        HYS = validate_hys(updated_values['HYSTERESIS'])
        if HYS != False:
            error_message += HYS

    if mode == "VDD":
        FAVD = validate_favd(updated_values['FIXED AV DELAY'])
        if FAVD != False:
            error_message += FAVD

        VA = validate_pa(updated_values['VENTRICULAR AMPLITUDE'])
        if VA != False:
            error_message += VA

        VPW = validate_pw(updated_values['VENTRICULAR PULSE WIDTH'])
        if VPW != False:
            error_message += VPW
        
        VS = validate_sen(updated_values['VENTRICULAR SENSITIVITY'])
        if VS != False:
            error_message += VS

        VRP = validate_rp(updated_values['VRP'])
        if VRP != False:
            error_message += VRP

        PVARP_EXT = validate_pvarp_ext(updated_values['PVARP EXTENSION'])
        if PVARP_EXT != False:
            error_message += PVARP_EXT

        ATRD = validate_atrd(updated_values['ATR DURATION'])
        if ATRD != False:
            error_message += ATRD

        ATRFT = validate_atrft(updated_values['ATR FALLBACK TIME'])
        if ATRFT != False:
            error_message += ATRFT

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
    
# Validate PVARP Extension value entered by the user
def validate_pvarp_ext(value):
    try:
        val = float(value)
    except ValueError:
        return "PVARP Extension must be a number.\n"
    
    if (val < 0) or ((val > 0) and (val < 50)) or (val > 400):
        return "PVARP Extension must be 0ms or between 50 and 400ms.\n"
    elif (val % 10 != 0):
        return "PVARP Extension must be a multiple of 10ms between 50ms and 400ms.\n"
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
    
# Validate the Hysteresis value entered by the user
def validate_hys(value):
    try:
        val = float(value)
    except ValueError:
        return "Hysteresis must be a number.\n"
    
    if (30 <= val) and (val <= 50) and (val % 5 != 0):
        return "Hysteresis must be a multiple of 5 between 30ms and 50ms.\n"
    elif (50 < val) and (val <= 90) and (val % 1 != 0):
        return "Hysteresis must be a multiple of 1 between 50ms and 90ms.\n"
    elif (90 < val) and (val <= 175) and (val % 5 != 0):
        return "Hysteresis must be a multiple of 5 between 90ms and 175ms.\n"
    elif (val < 30) or (val > 175):
        return "Hysteresis must be between 30ms and 175ms.\n"
    else:
        return False
    
# Validate the Fixed AV Delay value entered by the user
def validate_favd(value):
    try:
        val = float(value)
    except ValueError:
        return "Fixed AV Delay must be a number.\n"
    
    if (val < 70) or (val > 300):
        return "Fixed AV Delay must be between 70ms and 300ms.\n"
    elif (val % 10 != 0):
        return "Fixed AV Delay must be a multiple of 10ms between 70ms and 300ms.\n"
    else:
        return False
    
# Validate ATR Duration value entered by the user
def validate_atrd(value):
    try:
        val = float(value)
    except ValueError:
        return "ATR Duration must be a number.\n"
    
    if not ((val == 10) or ((val >= 20) and (val <= 80)) or ((val >= 100) and (val <= 2000))):
        return "ATR Duration must be 10ms, in the range of 20-80ms or in the range of 100-2000ms.\n"
    elif ((val >= 20) and (val <= 80) and (val % 20 != 0)):
        return "ATR Duration must be a multiple of 20ms between 20ms and 80ms.\n"
    elif ((val >= 100) and (val <= 2000) and (val % 100 != 0)):
        return "ATR Duration must be a multiple of 100ms between 100ms and 2000ms.\n"
    else:
        return False

# Validate the ATR Fallback Time value entered by the user
def validate_atrft(value):
    try:
        val = float(value)
    except ValueError:
        return "ATR Fallback Time must be a number.\n"
    
    if (val < 1 or val > 5):
        return "ATR Fallback Time must be between 1 and 5 minutes.\n"
    elif (val % 1 != 0):
        return "ATR Fallback Time must be a multiple of 1 minute between 1 and 5 minutes.\n"
    else:
        return False