from enum import Enum

MODES = ['AOO', 'AAI', 'VOO', 'VVI']

PARAMETERS = ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Ventricular Amplitude", "Atrial Pulse Width", "Ventricular Pulse Width", "VRP", "ARP"]

PARAMS = [[1, 1, 1, 0, 1, 0, 0, 0], #AOO - 0
          [1, 1, 1, 0, 1, 0, 0, 1], #AAI - 1
          [1, 1, 0, 1, 0, 1, 0, 0], #VOO - 2
          [1, 1, 0, 1, 0, 1, 1, 0]]  #VVI - 3

PASSWORD_RULES = {
    'min_length': 8,
    'special_chars': r'[!@#$%^&*()-_+=]',
    'number_range': r'[0-9]',
    'upper_case': r'[A-Z]',
}

MAX_USER_COUNT = 10

DATABASE_DIR = "DCM\\data.db"

class States(Enum):
    WELCOME = 0
    DASHBOARD = 1