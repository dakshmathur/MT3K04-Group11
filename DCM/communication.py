import serial
import struct
import database as db
from settings import SER_BAUD_RATE, SER_COM_PORT,MODE_MAP, NOMINAL_VALUES, ACTIVITY_THRESHOLD_MAP

def pack_array(updated_values, mode, sim_status, send_recv):

    # Expand updated_values to include all the fields that don't get updated for that mode
    updated_values_EXPANDED = {}
    keys = list(NOMINAL_VALUES.keys())[1:]  # Exlude mode key
    for key in keys:
        uppercase_key = db.lower_to_upper(key)  # Convert key to uppercase
        if uppercase_key in updated_values:
            updated_values_EXPANDED[uppercase_key] = updated_values[uppercase_key]
        else:
            updated_values_EXPANDED[uppercase_key] = NOMINAL_VALUES[key]

    values = updated_values_EXPANDED.copy()
    values['MODE'] = mode
    values['ATRIAL THRESHOLD'] = updated_values_EXPANDED['ATRIAL SENSITIVITY']
    values['VENTRICULAR THRESHOLD'] = updated_values_EXPANDED['VENTRICULAR SENSITIVITY']

    sorted_values = sort_dictionary(values)
    intify_values = intify(sorted_values)
    
    packed_array = [sim_status, send_recv]

    for key in intify_values:
        packed_array.append(intify_values[key])

    #print(intify_values)
    #print(packed_array)
    return packed_array

def sort_dictionary(d):
    order = ['mode',
            'lower_rate_limit',
            'upper_rate_limit',
            'pvarp',
            'fixed_av_delay',
            'reaction_time',
            'response_factor',
            'activity_threshold',
            'recovery_time',
            'maximum_sensor_rate',
            'atrial_amplitude',
            'atrial_pulse_width',
            'arp',
            'atrial_threshold',
            'atrial_sensitivity',
            'ventricular_amplitude',
            'ventricular_pulse_width',
            'vrp',
            'ventricular_threshold',
            'ventricular_sensitivity',
    ]

    sorted_dictionary = {}
    for key in order:
        if key == 'atrial_threshold' or key == 'ventricular_threshold':
            sorted_dictionary[key] = d['ATRIAL THRESHOLD'] if key == 'atrial_threshold' else d['VENTRICULAR THRESHOLD']
        else:
            sorted_dictionary[key] = d[db.lower_to_upper(key)]

    return sorted_dictionary


def intify(values):
    values_intify = values.copy()

    to_modify = ['mode', 'dynamic_av_delay', 'sensed_av_delay_offset', 'atrial_amplitude', 'ventricular_amplitude', 'pvarp_extension', 'hysteresis', 'rate_smoothing', 'atr_fallback_mode', 'activity_threshold']
    for key in values_intify:
        for key2 in to_modify:
        
            if key == key2:
                
                if key == 'mode':
                    values_intify[key] = MODE_MAP[values[key]]
                elif key == 'dynamic_av_delay':
                    values_intify[key] = 0 if values[key] == 'Off' else 1
                elif key == 'sensed_av_delay_offset':
                    values_intify[key] = 0 if (values[key] == 0 or values[key] == 'Off') else values[key]
                elif key == 'atrial_amplitude':
                    values_intify[key] = 0 if values[key] == 'Off' else values[key]
                elif key == 'ventricular_amplitude':
                    values_intify[key] = 0 if values[key] == 'Off' else values[key]
                elif key == 'pvarp_extension':
                    values_intify[key] = 0 if values[key] == 'Off' else values[key]
                elif key == 'hysteresis':
                    values_intify[key] = 0 if values[key] == 'Off' else values[key]
                elif key == 'rate_smoothing':
                    values_intify[key] = 0 if values[key] == 'Off' else values[key][-1]
                elif key == 'atr_fallback_mode':
                    values_intify[key] = 0 if values[key] == 'Off' else 1
                elif key == 'activity_threshold':
                    values_intify[key] = ACTIVITY_THRESHOLD_MAP[values[key]]


    for key in values_intify:
        if type(values_intify[key]) == int or type(values_intify[key]) == float:
            pass
        elif '.' in values_intify[key]:
            values_intify[key] = float(values_intify[key])
        else:
            values_intify[key] = int(values_intify[key])
        
    return values_intify

def txSer(updated_values, mode, sim_status, send_recv):
    dataArray = pack_array(updated_values, mode, sim_status, send_recv)
    dataArray.append(1) #LED RED AND GREEN
    dataArray.append(1)
    dataTuple = tuple(dataArray)
    dataStruct = struct.Struct('<BBHHHHHHHdHHdHHdddHHddBB')
    dataPacked = dataStruct.pack(*dataTuple)

    try:
        baudrate = SER_BAUD_RATE
        port = SER_COM_PORT
        #print("Now Sending: ", dataTuple, " to port: ", port)
        
        dataSentArray = list(dataTuple[2:-2])
        dataSentArrayFloat = [float(x) for x in dataSentArray]

        with serial.Serial(port, baudrate=baudrate, timeout=1) as ser:
            ser.write(dataPacked)
            return dataSentArrayFloat
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return [0]

def rxSer():
    dataStruct = struct.Struct('<HHHHHHHdHHdHHdddHHdddd')

    try:
        baudrate = SER_BAUD_RATE
        port = SER_COM_PORT
        with serial.Serial(port, baudrate=baudrate, timeout=1) as ser:
            dataReceived = ser.read(dataStruct.size)

            if dataReceived:
                dataTuple = dataStruct.unpack(dataReceived)
                dataRecievedArray = list(dataTuple[:-2])
                dataRecievedArrayFloat = [float(x) for x in dataRecievedArray]
                return dataRecievedArrayFloat
            else:
                print("No data received")
                return None
    except serial.SerialException as e:
        print(f"Error reading from serial port: {e}")
        return None
    
# def get_last_two_values(dataRecievedArrayFloat):
#     if len(dataRecievedArrayFloat) >= 2:
#         last_two_values = dataRecievedArrayFloat[-2:]  # Get the last two values
#         return last_two_values
#     else:
#         print("Not enough values in the array")
#         return None