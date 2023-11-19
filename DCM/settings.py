from enum import Enum

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

RATE_SMOOTHING_OPTIONS = ["Off", "3%", "6%", "9%", "12%", "15%", "18%", "21%", "25%"]