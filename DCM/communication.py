import serial
import struct
import database as db
from settings import SER_BAUD_RATE, MODE_MAP, NOMINAL_VALUES, ACTIVITY_THRESHOLD_MAP

def pack_array(updated_values, mode):
    print("\n\n")
    print("Updated Values ORIGINAL", updated_values)
        
    # Expand updated_values to include all the fields that don't get updated for that mode
    updated_values_EXPANDED = {}
    keys = list(NOMINAL_VALUES.keys())[1:]  # Exlude mode key
    for key in keys:
        uppercase_key = db.lower_to_upper(key)  # Convert key to uppercase
        if uppercase_key in updated_values:
            updated_values_EXPANDED[uppercase_key] = updated_values[uppercase_key]
        else:
            updated_values_EXPANDED[uppercase_key] = NOMINAL_VALUES[key]
    
    print("\n\n")
    print("Updated Values EXPANDED", updated_values_EXPANDED)

    values = updated_values_EXPANDED.copy()
    values['MODE'] = mode

    intify_values = intify(values)
    
    packed_array = []

    for key in intify_values:
        packed_array.append(intify_values[key])

    print("\n\n")
    print("Packed Array FINAL", packed_array)
    return packed_array

def intify(values):
    values_intify = NOMINAL_VALUES.copy()

    to_modify = ['mode', 'dynamic_av_delay', 'sensed_av_delay_offset', 'atrial_amplitude', 'ventricular_amplitude', 'pvarp_extension', 'hysteresis', 'rate_smoothing', 'atr_fallback_mode', 'activity_threshold']
    for key in values_intify:
        for key2 in to_modify:
        
            if key == key2:

                if key == 'mode':
                    values_intify[key] = MODE_MAP[values[db.lower_to_upper(key)]]
                elif key == 'dynamic_av_delay':
                    values_intify[key] = 0 if values[db.lower_to_upper(key)] == 'Off' else 1
                elif key == 'sensed_av_delay_offset':
                    values_intify[key] = 0 if (values[db.lower_to_upper(key)] == 0 or values[db.lower_to_upper(key)] == 'Off') else values[db.lower_to_upper(key)]
                elif key == 'atrial_amplitude':
                    values_intify[key] = 0 if values[db.lower_to_upper(key)] == 'Off' else values[db.lower_to_upper(key)]
                elif key == 'ventricular_amplitude':
                    values_intify[key] = 0 if values[db.lower_to_upper(key)] == 'Off' else values[db.lower_to_upper(key)]
                elif key == 'pvarp_extension':
                    values_intify[key] = 0 if values[db.lower_to_upper(key)] == 'Off' else values[db.lower_to_upper(key)]
                elif key == 'hysteresis':
                    values_intify[key] = 0 if values[db.lower_to_upper(key)] == 'Off' else values[db.lower_to_upper(key)]
                elif key == 'rate_smoothing':
                    values_intify[key] = 0 if values[db.lower_to_upper(key)] == 'Off' else values[db.lower_to_upper(key)][-1]
                elif key == 'atr_fallback_mode':
                    values_intify[key] = 0 if values[db.lower_to_upper(key)] == 'Off' else 1
                elif key == 'activity_threshold':
                    values_intify[key] = ACTIVITY_THRESHOLD_MAP[values[db.lower_to_upper(key)]]
        
    return values_intify

def txSer(updated_values, mode, port):
    dataAray = pack_array(updated_values, mode)
    dataAray.append([0,0])
    dataTuple = tuple(dataAray)
    dataStruct = struct.Struct('<<BBBBHBbfBfBffHHHHBBBHBBBBBBB')
    dataPacked = dataStruct.pack(*dataTuple)

    try:
        baudrate = SER_BAUD_RATE
        with serial.Serial(port, baudrate=baudrate, timeout=1) as ser:
            ser.write(dataPacked)
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
