import os
from enum import Enum

PASSWORD_RULES = {
    'min_length': 8,
    'special_chars': r'[!@#$%^&*()-_+=]',
    'number_range': r'[0-9]',
    'upper_case': r'[A-Z]',
}

MAX_USER_COUNT = 10

DATABASE_DIR = "DCM\\data.db"

RUNNING_DIR = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_IMAGE_DIR = os.path.join(RUNNING_DIR, 'NewBackround.jpg')

class States(Enum):
    WELCOME = 0
    DASHBOARD = 1

RATE_SMOOTHING_OPTIONS = ["Off", "3%", "6%", "9%", "12%", "15%", "18%", "21%", "25%"]

ACTIVITY_THRESHOLD_OPTIONS = ["V-Low", "Low", "Med-Low", "Med", "Med-High", "High", "V-High"]

NOMINAL_VALUES = {
    "mode": "DDD",
    "lower_rate_limit": 60,
    "upper_rate_limit": 120,
    "maximum_sensor_rate": 120,
    "fixed_av_delay": 150,
    "dynamic_av_delay": "Off",
    "sensed_av_delay_offset": "Off",
    "atrial_amplitude": 5,
    "atrial_pulse_width": 1,
    "ventricular_amplitude": 5,
    "ventricular_pulse_width": 1,
    "atrial_sensitivity": 0,
    "ventricular_sensitivity": 2.5,
    "arp": 250,
    "pvarp": 250,
    "pvarp_extension": "Off",
    "vrp": 320,
    "hysteresis": "Off",
    "rate_smoothing": "Off",
    "atr_fallback_mode": "Off",
    "atr_duration": 20,
    "atr_fallback_time": 1,
    "activity_threshold": "Med",
    "reaction_time": 30,
    "response_factor": 8,
    "recovery_time": 5
}

PARAMETER_UNITS = {
    "mode": "",
    "lower_rate_limit": "ppm",
    "upper_rate_limit": "ppm",
    "maximum_sensor_rate": "ppm",
    "fixed_av_delay": "ms",
    "dynamic_av_delay": "",
    "sensed_av_delay_offset": "ms",
    "atrial_amplitude": "V",
    "atrial_pulse_width": "ms",
    "ventricular_amplitude": "V",
    "ventricular_pulse_width": "ms",
    "atrial_sensitivity": "V",
    "ventricular_sensitivity": "V",
    "arp": "ms",
    "vrp": "ms",
    "pvarp": "ms",
    "pvarp_extension": "ms",
    "hysteresis": "ms",
    "rate_smoothing": "%",
    "atr_fallback_mode": "",
    "atr_duration": "cc",
    "atr_fallback_time": "min",
    "activity_threshold": "",
    "reaction_time": "sec",
    "response_factor": "",
    "recovery_time": "min"
}

MODE_MAP = {
    "AAT": 0,
    "VVT": 1,
    "AOO": 2,
    "AAI": 3,
    "VOO": 4,
    "VVI": 5,
    "VDD": 6,
    "DOO": 7,
    "DDI": 8,
    "DDD": 9,
    "AOOR": 10,
    "AAIR": 11,
    "VOOR": 12,
    "VVIR": 13,
    "VDDR": 14,
    "DOOR": 15,
    "DDIR": 16,
    "DDDR": 17
}

DYNAMIC_AV_DELAY_MAP = {
    "Off": 0,
    "On": 1
}

ACTIVITY_THRESHOLD_MAP = {
    "V-Low": 0,
    "Low": 1,
    "Med-Low": 2,
    "Med": 3,
    "Med-High": 4,
    "High": 5,
    "V-High": 6
}