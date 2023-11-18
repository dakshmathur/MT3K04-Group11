import sqlite3
from settings import DATABASE_DIR

connect = sqlite3.connect(DATABASE_DIR)
cursor = connect.cursor()

def createDB():
    cursor.execute("""
        CREATE TABLE aoo (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER
        );              
    """)

    cursor.execute("""
        CREATE TABLE aai (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            atrial_sensitivity NUMBER,
            arp NUMBER,
            pvarp NUMBER,
            hysteresis NUMBER,
            rate_smoothing NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE voo (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER
        );
    """)

    cursor.execute("""               
        CREATE TABLE vvi (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            ventricular_sensitivity NUMBER,
            vrp NUMBER,
            hysteresis NUMBER,
            rate_smoothing NUMBER
        );
    """)

    cursor.execute("""               
        CREATE TABLE users (
            id NUMBER PRIMARY KEY, 
            username TEXT, 
            password TEXT, 
            current_mode TEXT
        );
    """)

def get_num_users():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

def get_username(id):
    cursor.execute("SELECT username FROM users WHERE id = ?", (id,))
    return cursor.fetchone()[0]

def get_user_id(username):
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    return cursor.fetchone()[0]

def get_password(id):
    cursor.execute("SELECT password FROM users WHERE id = ?", (id,))
    return cursor.fetchone()[0]

def create_user(username, password):
    num_users = get_num_users()
    cursor.execute("""
        INSERT INTO aoo (
            id, 
            lower_rate_limit, 
            upper_rate_limit, 
            atrial_amplitude, 
            atrial_pulse_width
        ) 
        VALUES (?, ?, ?, ?, ?)""", (num_users,60,120,3.5,0.4))
    
    cursor.execute("""
        INSERT INTO aai (
            id,
            lower_rate_limit,
            upper_rate_limit,
            atrial_amplitude,
            atrial_pulse_width,
            atrial_sensitivity,
            arp,
            pvarp,
            hysteresis,
            rate_smoothing
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users,60,120,3.5,0.4,0.75,250,250,0,"Off")
    )
    
    cursor.execute("""
        INSERT INTO voo (
            id,
            lower_rate_limit,
            upper_rate_limit,
            ventricular_amplitude,
            ventricular_pulse_width
        )
        VALUES (?, ?, ?, ?, ?)""", (num_users,60,120,3.5,0.4)
    )
    
    cursor.execute("""
        INSERT INTO vvi (
            id,
            lower_rate_limit,
            upper_rate_limit,
            ventricular_amplitude,
            ventricular_pulse_width,
            ventricular_sensitivity,
            vrp,
            hysteresis,
            rate_smoothing
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users,60,120,3.5,0.4,2.5,320,0,"Off")
    )
    
    cursor.execute("""
        INSERT INTO users (
            id, 
            username, 
            password, 
            current_mode
            )
            VALUES (?, ?, ?, ?)""", (num_users, username, password, "aoo")
    )
    
    connect.commit()
    return True

def update_mode(id, mode):
    cursor.execute("UPDATE users SET current_mode = ? WHERE id = ?", (mode, id))
    connect.commit()

def get_mode(id):
    cursor.execute("SELECT current_mode FROM users WHERE id = ?", (id,))
    return cursor.fetchone()[0]

def lookup_parameter_value(id, mode, parameter):
    cursor.execute("SELECT " + parameter.lower().replace(" ", "_") + " FROM " + mode + " WHERE id = ?", (id,))
    return cursor.fetchone()[0]
    
# return a dictionary of the parameters for the current mode of the user and the values for those parameters in the database
def get_mode_parameters(id):
    mode_parameters = {}
    mode = get_mode(id)

    cursor.execute("SELECT * FROM " + mode + " WHERE id = ?", (id,))
    working_list = [description[0] for description in cursor.description][1:]

    for i in range(len(working_list)):
        working_list[i] = working_list[i].replace("_", " ").title()

        if working_list[i][-2:] == "rp":
            working_list[i] = working_list[i].upper()

        mode_parameters[working_list[i]] = lookup_parameter_value(id, mode, working_list[i])

    return mode_parameters

def update_mode_parameters(id, mode, updated_values):
    try:
        columns_map = {
            'AOO': ['lower_rate_limit', 'upper_rate_limit', 'atrial_amplitude', 'atrial_pulse_width'],
            'AAI': ['lower_rate_limit', 'upper_rate_limit', 'atrial_amplitude', 'atrial_pulse_width', 'atrial_sensitivity', 'arp', 'pvarp', 'hysteresis', 'rate_smoothing'],
            'VOO': ['lower_rate_limit', 'upper_rate_limit', 'ventricular_amplitude', 'ventricular_pulse_width'],
            'VVI': ['lower_rate_limit', 'upper_rate_limit', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp', 'hysteresis', 'rate_smoothing'],
            # Add mappings for other modes
        }

        def transform_column_name(col):
            if col in ['arp', 'vrp', 'pvarp']:
                return col.upper()
            else:
                return col.replace('_', ' ').title()

        # Select the columns for the current mode
        columns = columns_map.get(mode, [])
        if not columns:
            print(f"No column mapping found for mode: {mode}")

        # Construct the SQL query dynamically
        set_clause = ', '.join([f"{col} = ?" for col in columns])
        sql_query = f"UPDATE {mode.lower()} SET {set_clause} WHERE id = ?"

        # Prepare the values for the SQL query
        values = [updated_values.get(transform_column_name(column), None) for column in columns]
        values.append(id)  # Append the user ID at the end

        # Execute the query
        cursor.execute(sql_query, values)
        connect.commit()
    except Exception as e:
        # Handle any exceptions (e.g., log them, inform the user)
        print(f"Error updating mode parameters: {e}")


def get_all_modes():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'users'")
    return [mode[0].upper() for mode in cursor.fetchall()]


