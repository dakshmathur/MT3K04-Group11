import struct
import database as db
from settings import MODE_MAP, NOMINAL_VALUES, ACTIVITY_THRESHOLD_MAP

def pack_array(updated_values, mode):
    values = updated_values.copy()
    values['MODE'] = mode

    intify_values = intify(values)
    
    packed_array = []

    for key in intify_values:
        packed_array.append(intify_values[key])

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
                    values_intify[key] = 0 if values[db.lower_to_upper(key)] == 0 else values[db.lower_to_upper(key)]
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