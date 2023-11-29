import sqlite3
from settings import DATABASE_DIR, NOMINAL_VALUES

connect = sqlite3.connect(DATABASE_DIR)
cursor = connect.cursor()

def createDB():
    cursor.execute("""
        CREATE TABLE aat (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            atrial_sensitivity NUMBER,
            arp NUMBER,
            pvarp NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE vvt (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            ventricular_sensitivity NUMBER,
            vrp NUMBER
        );
    """)
                   
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
        CREATE TABLE vdd (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            fixed_av_delay NUMBER,
            dynamic_av_delay TEXT,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            ventricular_sensitivity NUMBER,
            vrp NUMBER,
            pvarp_extension NUMBER,
            rate_smoothing NUMBER,
            atr_duration NUMBER,
            atr_fallback_mode TEXT,
            atr_fallback_time NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE doo (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            fixed_av_delay NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE ddi (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            fixed_av_delay NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            atrial_sensitivity NUMBER,
            ventricular_sensitivity NUMBER,
            vrp NUMBER,
            arp NUMBER,
            pvarp NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE ddd (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            fixed_av_delay NUMBER,
            dynamic_av_delay TEXT,
            sensed_av_delay_offset NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            atrial_sensitivity NUMBER,
            ventricular_sensitivity NUMBER,
            vrp NUMBER,
            arp NUMBER,
            pvarp NUMBER,
            pvarp_extension NUMBER,
            hysteresis NUMBER,
            rate_smoothing NUMBER,
            atr_duration NUMBER,
            atr_fallback_mode TEXT,
            atr_fallback_time NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE aoor (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            maximum_sensor_rate NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            activity_threshold NUMBER,
            reaction_time NUMBER,
            response_factor NUMBER,
            recovery_time NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE aair (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            maximum_sensor_rate NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            atrial_sensitivity NUMBER,
            arp NUMBER,
            pvarp NUMBER,
            hysteresis NUMBER,
            rate_smoothing NUMBER,
            activity_threshold NUMBER,
            reaction_time NUMBER,
            response_factor NUMBER,
            recovery_time NUMBER
        );           
    """)

    cursor.execute("""
        CREATE TABLE voor (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            maximum_sensor_rate NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            activity_threshold NUMBER,
            reaction_time NUMBER,
            response_factor NUMBER,
            recovery_time NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE vvir (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            maximum_sensor_rate NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            ventricular_sensitivity NUMBER,
            vrp NUMBER,
            hysteresis NUMBER,
            rate_smoothing NUMBER,
            activity_threshold NUMBER,
            reaction_time NUMBER,
            response_factor NUMBER,
            recovery_time NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE vddr (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            maximum_sensor_rate NUMBER,
            fixed_av_delay NUMBER,
            dynamic_av_delay TEXT,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            ventricular_sensitivity NUMBER,
            vrp NUMBER,
            pvarp_extension NUMBER,
            rate_smoothing NUMBER,
            atr_duration NUMBER,
            atr_fallback_mode TEXT,
            atr_fallback_time NUMBER,
            activity_threshold NUMBER,
            reaction_time NUMBER,
            response_factor NUMBER,
            recovery_time NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE door (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            maximum_sensor_rate NUMBER,
            fixed_av_delay NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            activity_threshold NUMBER,
            reaction_time NUMBER,
            response_factor NUMBER,
            recovery_time NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE ddir (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            maximum_sensor_rate NUMBER,
            fixed_av_delay NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            atrial_sensitivity NUMBER,
            ventricular_sensitivity NUMBER,
            vrp NUMBER,
            arp NUMBER,
            pvarp NUMBER,
            activity_threshold NUMBER,
            reaction_time NUMBER,
            response_factor NUMBER,
            recovery_time NUMBER
        );
    """)

    cursor.execute("""
        CREATE TABLE dddr (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            maximum_sensor_rate NUMBER,
            fixed_av_delay NUMBER,
            dynamic_av_delay TEXT,
            sensed_av_delay_offset NUMBER,
            atrial_amplitude NUMBER,
            atrial_pulse_width NUMBER,
            ventricular_amplitude NUMBER,
            ventricular_pulse_width NUMBER,
            atrial_sensitivity NUMBER,
            ventricular_sensitivity NUMBER,
            vrp NUMBER,
            arp NUMBER,
            pvarp NUMBER,
            pvarp_extension NUMBER,
            hysteresis NUMBER,
            rate_smoothing NUMBER,
            atr_duration NUMBER,
            atr_fallback_mode TEXT,
            atr_fallback_time NUMBER,
            activity_threshold NUMBER,
            reaction_time NUMBER,
            response_factor NUMBER,
            recovery_time NUMBER
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
    cursor.execute("""INSERT INTO aat (
        id,
        lower_rate_limit,
        upper_rate_limit,
        atrial_amplitude,
        atrial_pulse_width,
        atrial_sensitivity,
        arp,
        pvarp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (num_users,NOMINAL_VALUES["lower_rate_limit"],NOMINAL_VALUES["upper_rate_limit"],NOMINAL_VALUES["atrial_amplitude"],NOMINAL_VALUES["atrial_pulse_width"],NOMINAL_VALUES["atrial_sensitivity"],NOMINAL_VALUES["arp"],NOMINAL_VALUES["pvarp"])
    )

    cursor.execute("""INSERT INTO vvt (
        id,
        lower_rate_limit,
        upper_rate_limit,
        ventricular_amplitude,
        ventricular_pulse_width,
        ventricular_sensitivity,
        vrp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)""", (num_users,NOMINAL_VALUES["lower_rate_limit"],NOMINAL_VALUES["upper_rate_limit"],NOMINAL_VALUES["ventricular_amplitude"],NOMINAL_VALUES["ventricular_pulse_width"],NOMINAL_VALUES["ventricular_sensitivity"],NOMINAL_VALUES["vrp"])
    )

    cursor.execute("""
        INSERT INTO aoo (
            id, 
            lower_rate_limit, 
            upper_rate_limit, 
            atrial_amplitude, 
            atrial_pulse_width
        ) 
        VALUES (?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"])
    )
    
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"], NOMINAL_VALUES["atrial_sensitivity"], NOMINAL_VALUES["arp"], NOMINAL_VALUES["pvarp"], NOMINAL_VALUES["hysteresis"], NOMINAL_VALUES["rate_smoothing"])
    )
    
    cursor.execute("""
        INSERT INTO voo (
            id,
            lower_rate_limit,
            upper_rate_limit,
            ventricular_amplitude,
            ventricular_pulse_width
        )
        VALUES (?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"])
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["ventricular_sensitivity"], NOMINAL_VALUES["vrp"], NOMINAL_VALUES["hysteresis"], NOMINAL_VALUES["rate_smoothing"])
    )

    cursor.execute("""
        INSERT INTO vdd (
            id,
            lower_rate_limit,
            upper_rate_limit,
            fixed_av_delay,
            dynamic_av_delay,
            ventricular_amplitude,
            ventricular_pulse_width,
            ventricular_sensitivity,
            vrp,
            pvarp_extension,
            rate_smoothing,
            atr_duration,
            atr_fallback_mode,
            atr_fallback_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["fixed_av_delay"], NOMINAL_VALUES["dynamic_av_delay"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["ventricular_sensitivity"], NOMINAL_VALUES["vrp"], NOMINAL_VALUES["pvarp_extension"], NOMINAL_VALUES["rate_smoothing"], NOMINAL_VALUES["atr_duration"], NOMINAL_VALUES["atr_fallback_mode"], NOMINAL_VALUES["atr_fallback_time"])
    )

    cursor.execute("""
        INSERT INTO doo (
            id,
            lower_rate_limit,
            upper_rate_limit,
            fixed_av_delay,
            atrial_amplitude,
            atrial_pulse_width,
            ventricular_amplitude,
            ventricular_pulse_width
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["fixed_av_delay"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"])
    )

    cursor.execute("""
        INSERT INTO ddi (
            id,
            lower_rate_limit,
            upper_rate_limit,
            fixed_av_delay,
            atrial_amplitude,
            atrial_pulse_width,
            atrial_sensitivity,
            ventricular_amplitude,
            ventricular_pulse_width,
            ventricular_sensitivity,
            vrp,
            arp,
            pvarp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["fixed_av_delay"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"], NOMINAL_VALUES["atrial_sensitivity"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["ventricular_sensitivity"], NOMINAL_VALUES["vrp"], NOMINAL_VALUES["arp"], NOMINAL_VALUES["pvarp"])
    )

    cursor.execute("""
        INSERT INTO ddd (
            id,
            lower_rate_limit,
            upper_rate_limit,
            fixed_av_delay,
            dynamic_av_delay,
            sensed_av_delay_offset,
            atrial_amplitude,
            atrial_pulse_width,
            atrial_sensitivity,
            arp,
            pvarp,
            pvarp_extension,
            ventricular_amplitude,
            ventricular_pulse_width,
            ventricular_sensitivity,
            vrp,
            hysteresis,
            rate_smoothing,
            atr_duration,
            atr_fallback_mode,
            atr_fallback_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["fixed_av_delay"], NOMINAL_VALUES["dynamic_av_delay"], NOMINAL_VALUES["sensed_av_delay_offset"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"], NOMINAL_VALUES["atrial_sensitivity"], NOMINAL_VALUES["arp"], NOMINAL_VALUES["pvarp"], NOMINAL_VALUES["pvarp_extension"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["ventricular_sensitivity"], NOMINAL_VALUES["vrp"], NOMINAL_VALUES["hysteresis"], NOMINAL_VALUES["rate_smoothing"], NOMINAL_VALUES["atr_duration"], NOMINAL_VALUES["atr_fallback_mode"], NOMINAL_VALUES["atr_fallback_time"])
    )

    cursor.execute("""
        INSERT INTO aoor (
            id,
            lower_rate_limit,
            upper_rate_limit,
            maximum_sensor_rate,
            atrial_amplitude,
            atrial_pulse_width,
            activity_threshold,
            reaction_time,
            response_factor,
            recovery_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["maximum_sensor_rate"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"], NOMINAL_VALUES["activity_threshold"], NOMINAL_VALUES["reaction_time"], NOMINAL_VALUES["response_factor"], NOMINAL_VALUES["recovery_time"])
    )

    cursor.execute("""
        INSERT INTO aair (
            id,
            lower_rate_limit,
            upper_rate_limit,
            maximum_sensor_rate,
            atrial_amplitude,
            atrial_pulse_width,
            atrial_sensitivity,
            arp,
            pvarp,
            hysteresis,
            rate_smoothing,
            activity_threshold,
            reaction_time,
            response_factor,
            recovery_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["maximum_sensor_rate"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"], NOMINAL_VALUES["atrial_sensitivity"], NOMINAL_VALUES["arp"], NOMINAL_VALUES["pvarp"], NOMINAL_VALUES["hysteresis"], NOMINAL_VALUES["rate_smoothing"], NOMINAL_VALUES["activity_threshold"], NOMINAL_VALUES["reaction_time"], NOMINAL_VALUES["response_factor"], NOMINAL_VALUES["recovery_time"])
    )

    cursor.execute("""
        INSERT INTO voor (
            id,
            lower_rate_limit,
            upper_rate_limit,
            maximum_sensor_rate,
            ventricular_amplitude,
            ventricular_pulse_width,
            activity_threshold,
            reaction_time,
            response_factor,
            recovery_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["maximum_sensor_rate"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["activity_threshold"], NOMINAL_VALUES["reaction_time"], NOMINAL_VALUES["response_factor"], NOMINAL_VALUES["recovery_time"])
    )

    cursor.execute("""
        INSERT INTO vvir (
            id,
            lower_rate_limit,
            upper_rate_limit,
            maximum_sensor_rate,
            ventricular_amplitude,
            ventricular_pulse_width,
            ventricular_sensitivity,
            vrp,
            hysteresis,
            rate_smoothing,
            activity_threshold,
            reaction_time,
            response_factor,
            recovery_time
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["maximum_sensor_rate"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["ventricular_sensitivity"], NOMINAL_VALUES["vrp"], NOMINAL_VALUES["hysteresis"], NOMINAL_VALUES["rate_smoothing"], NOMINAL_VALUES["activity_threshold"], NOMINAL_VALUES["reaction_time"], NOMINAL_VALUES["response_factor"], NOMINAL_VALUES["recovery_time"])
    )

    cursor.execute("""
        INSERT INTO vddr (
            id,
            lower_rate_limit,
            upper_rate_limit,
            maximum_sensor_rate,
            fixed_av_delay,
            dynamic_av_delay,
            ventricular_amplitude,
            ventricular_pulse_width,
            ventricular_sensitivity,
            vrp,
            pvarp_extension,
            rate_smoothing,
            atr_duration,
            atr_fallback_mode,
            atr_fallback_time,
            activity_threshold,
            reaction_time,
            response_factor,
            recovery_time
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["maximum_sensor_rate"], NOMINAL_VALUES["fixed_av_delay"], NOMINAL_VALUES["dynamic_av_delay"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["ventricular_sensitivity"], NOMINAL_VALUES["vrp"], NOMINAL_VALUES["pvarp_extension"], NOMINAL_VALUES["rate_smoothing"], NOMINAL_VALUES["atr_duration"], NOMINAL_VALUES["atr_fallback_mode"], NOMINAL_VALUES["atr_fallback_time"], NOMINAL_VALUES["activity_threshold"], NOMINAL_VALUES["reaction_time"], NOMINAL_VALUES["response_factor"], NOMINAL_VALUES["recovery_time"])
    )

    cursor.execute("""
        INSERT INTO door (
            id,
            lower_rate_limit,
            upper_rate_limit,
            maximum_sensor_rate,
            fixed_av_delay,
            atrial_amplitude,
            atrial_pulse_width,
            ventricular_amplitude,
            ventricular_pulse_width,
            activity_threshold,
            reaction_time,
            response_factor,
            recovery_time
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["maximum_sensor_rate"], NOMINAL_VALUES["fixed_av_delay"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["activity_threshold"], NOMINAL_VALUES["reaction_time"], NOMINAL_VALUES["response_factor"], NOMINAL_VALUES["recovery_time"])
    )

    cursor.execute("""
        INSERT INTO ddir (
            id,
            lower_rate_limit,
            upper_rate_limit,
            maximum_sensor_rate,
            fixed_av_delay,
            atrial_amplitude,
            atrial_pulse_width,
            ventricular_amplitude,
            ventricular_pulse_width,
            atrial_sensitivity,
            ventricular_sensitivity,
            vrp,
            arp,
            pvarp,
            activity_threshold,
            reaction_time,
            response_factor,
            recovery_time
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["maximum_sensor_rate"], NOMINAL_VALUES["fixed_av_delay"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["atrial_sensitivity"], NOMINAL_VALUES["ventricular_sensitivity"], NOMINAL_VALUES["vrp"], NOMINAL_VALUES["arp"], NOMINAL_VALUES["pvarp"], NOMINAL_VALUES["activity_threshold"], NOMINAL_VALUES["reaction_time"], NOMINAL_VALUES["response_factor"], NOMINAL_VALUES["recovery_time"])
    )

    cursor.execute("""
        INSERT INTO dddr (
            id,
            lower_rate_limit,
            upper_rate_limit,
            maximum_sensor_rate,
            fixed_av_delay,
            dynamic_av_delay,
            sensed_av_delay_offset,
            atrial_amplitude,
            atrial_pulse_width,
            ventricular_amplitude,
            ventricular_pulse_width,
            atrial_sensitivity,
            ventricular_sensitivity,
            vrp,
            arp,
            pvarp,
            pvarp_extension,
            hysteresis,
            rate_smoothing,
            atr_duration,
            atr_fallback_mode,
            atr_fallback_time,
            activity_threshold,
            reaction_time,
            response_factor,
            recovery_time
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (num_users, NOMINAL_VALUES["lower_rate_limit"], NOMINAL_VALUES["upper_rate_limit"], NOMINAL_VALUES["maximum_sensor_rate"], NOMINAL_VALUES["fixed_av_delay"], NOMINAL_VALUES["dynamic_av_delay"], NOMINAL_VALUES["sensed_av_delay_offset"], NOMINAL_VALUES["atrial_amplitude"], NOMINAL_VALUES["atrial_pulse_width"], NOMINAL_VALUES["ventricular_amplitude"], NOMINAL_VALUES["ventricular_pulse_width"], NOMINAL_VALUES["atrial_sensitivity"], NOMINAL_VALUES["ventricular_sensitivity"], NOMINAL_VALUES["vrp"], NOMINAL_VALUES["arp"], NOMINAL_VALUES["pvarp"], NOMINAL_VALUES["pvarp_extension"], NOMINAL_VALUES["hysteresis"], NOMINAL_VALUES["rate_smoothing"], NOMINAL_VALUES["atr_duration"], NOMINAL_VALUES["atr_fallback_mode"], NOMINAL_VALUES["atr_fallback_time"], NOMINAL_VALUES["activity_threshold"], NOMINAL_VALUES["reaction_time"], NOMINAL_VALUES["response_factor"], NOMINAL_VALUES["recovery_time"])
    )

    cursor.execute("""
        INSERT INTO users (
            id, 
            username, 
            password, 
            current_mode
            )
            VALUES (?, ?, ?, ?)""", (num_users, username, password, NOMINAL_VALUES["mode"])
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
    cursor.execute("SELECT " + upper_to_lower(parameter) + " FROM " + mode + " WHERE id = ?", (id,))
    res = cursor.fetchone()[0]
    if res == "On":
        return True
    elif res == "Off":
        return False
    else:
        return res
    
# return a dictionary of the parameters for the current mode of the user and the values for those parameters in the database
def get_mode_parameters(id):
    mode_parameters = {}
    mode = get_mode(id)

    cursor.execute("SELECT * FROM " + mode + " WHERE id = ?", (id,))
    working_list = [description[0] for description in cursor.description][1:]

    for i in range(len(working_list)):
        working_list[i] = lower_to_upper(working_list[i])

        if working_list[i][-2:] == "rp":
            working_list[i] = working_list[i].upper()

        mode_parameters[working_list[i]] = lookup_parameter_value(id, mode, working_list[i])

    return mode_parameters

def lower_to_upper(text):
    return text.replace('_', ' ').upper()

def upper_to_lower(text):
    return text.replace(' ', '_').lower()

def update_mode_parameters(id, mode, updated_values):
    try:
        columns_map = {
            'AAT': ['lower_rate_limit', 'upper_rate_limit', 'atrial_amplitude', 'atrial_pulse_width', 'atrial_sensitivity', 'arp', 'pvarp'],
            'VVT': ['lower_rate_limit', 'upper_rate_limit', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp'],
            'AOO': ['lower_rate_limit', 'upper_rate_limit', 'atrial_amplitude', 'atrial_pulse_width'],
            'AAI': ['lower_rate_limit', 'upper_rate_limit', 'atrial_amplitude', 'atrial_pulse_width', 'atrial_sensitivity', 'arp', 'pvarp', 'hysteresis', 'rate_smoothing'],
            'VOO': ['lower_rate_limit', 'upper_rate_limit', 'ventricular_amplitude', 'ventricular_pulse_width'],
            'VVI': ['lower_rate_limit', 'upper_rate_limit', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp', 'hysteresis', 'rate_smoothing'],
            'VDD': ['lower_rate_limit', 'upper_rate_limit', 'fixed_av_delay', 'dynamic_av_delay', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp', 'pvarp_extension', 'rate_smoothing', 'atr_duration', 'atr_fallback_mode', 'atr_fallback_time'],
            'DOO': ['lower_rate_limit', 'upper_rate_limit', 'fixed_av_delay', 'atrial_amplitude', 'atrial_pulse_width', 'ventricular_amplitude', 'ventricular_pulse_width'],
            'DDI': ['lower_rate_limit', 'upper_rate_limit', 'fixed_av_delay', 'atrial_amplitude', 'atrial_pulse_width', 'atrial_sensitivity', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp', 'arp', 'pvarp'],
            'DDD': ['lower_rate_limit', 'upper_rate_limit', 'fixed_av_delay', 'dynamic_av_delay', 'sensed_av_delay_offset', 'atrial_amplitude', 'atrial_pulse_width', 'atrial_sensitivity', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp', 'arp', 'pvarp', 'hysteresis', 'rate_smoothing', 'atr_duration', 'atr_fallback_mode', 'atr_fallback_time', 'pvarp_extension'],
            'AOOR': ['lower_rate_limit', 'upper_rate_limit', 'atrial_amplitude', 'atrial_pulse_width', 'maximum_sensor_rate', 'activity_threshold', 'reaction_time', 'response_factor', 'recovery_time'],
            'AAIR': ['lower_rate_limit', 'upper_rate_limit', 'atrial_amplitude', 'atrial_pulse_width', 'atrial_sensitivity', 'arp', 'pvarp', 'hysteresis', 'rate_smoothing', 'maximum_sensor_rate', 'activity_threshold', 'reaction_time', 'response_factor', 'recovery_time'],
            'VOOR': ['lower_rate_limit', 'upper_rate_limit', 'ventricular_amplitude', 'ventricular_pulse_width', 'maximum_sensor_rate', 'activity_threshold', 'reaction_time', 'response_factor', 'recovery_time'],
            'VVIR': ['lower_rate_limit', 'upper_rate_limit', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp', 'hysteresis', 'rate_smoothing', 'maximum_sensor_rate', 'activity_threshold', 'reaction_time', 'response_factor', 'recovery_time'],
            'VDDR': ['lower_rate_limit', 'upper_rate_limit', 'fixed_av_delay', 'dynamic_av_delay', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp', 'pvarp_extension', 'rate_smoothing', 'maximum_sensor_rate', 'activity_threshold', 'reaction_time', 'response_factor', 'recovery_time', 'atr_duration', 'atr_fallback_mode', 'atr_fallback_time'],
            'DOOR': ['lower_rate_limit', 'upper_rate_limit', 'fixed_av_delay', 'atrial_amplitude', 'atrial_pulse_width', 'ventricular_amplitude', 'ventricular_pulse_width', 'maximum_sensor_rate', 'activity_threshold', 'reaction_time', 'response_factor', 'recovery_time'],
            'DDIR': ['lower_rate_limit', 'upper_rate_limit', 'fixed_av_delay', 'atrial_amplitude', 'atrial_pulse_width', 'atrial_sensitivity', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp', 'arp', 'pvarp', 'maximum_sensor_rate', 'activity_threshold', 'reaction_time', 'response_factor', 'recovery_time'],
            'DDDR': ['lower_rate_limit', 'upper_rate_limit', 'fixed_av_delay', 'dynamic_av_delay', 'sensed_av_delay_offset', 'atrial_amplitude', 'atrial_pulse_width', 'atrial_sensitivity', 'ventricular_amplitude', 'ventricular_pulse_width', 'ventricular_sensitivity', 'vrp', 'arp', 'pvarp', 'hysteresis', 'rate_smoothing', 'maximum_sensor_rate', 'activity_threshold', 'reaction_time', 'response_factor', 'recovery_time', 'atr_duration', 'atr_fallback_mode', 'atr_fallback_time', 'pvarp_extension'],
        }
           
        # Select the columns for the current mode
        columns = columns_map.get(mode, [])
        if not columns:
            print(f"No column mapping found for mode: {mode}")

        # Construct the SQL query dynamically
        set_clause = ', '.join([f"{col} = ?" for col in columns])
        sql_query = f"UPDATE {mode.lower()} SET {set_clause} WHERE id = ?"

        # Prepare the values for the SQL query
        values = [updated_values.get(lower_to_upper(column), None) for column in columns]
        values.append(id)  # Append the user ID at the end

        # Execute the query
        cursor.execute(sql_query, values)
        connect.commit()

        return True    
    except Exception as e:
        # Handle any exceptions (e.g., log them, inform the user)
        print(f"Error updating mode parameters: {e}")
        return False


def get_all_modes():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'users'")
    return [mode[0].upper() for mode in cursor.fetchall()]

