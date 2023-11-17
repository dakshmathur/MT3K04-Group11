import sqlite3
#from settings import DATABASE_DIR

connect = sqlite3.connect("DCM\\data.db")
cursor = connect.cursor()

def createDB():
    cursor.execute("""
        CREATE TABLE aoo (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            atrial_amplitutde NUMBER,
            atrial_pulse_width NUMBER
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
        CREATE TABLE aai (
            id NUMBER PRIMARY KEY,
            lower_rate_limit NUMBER,
            upper_rate_limit NUMBER,
            atrial_amplitutde NUMBER,
            atrial_pulse_width NUMBER,
            atrial_sensitivity NUMBER,
            arp NUMBER,
            pvarp NUMBER,
            hysterisis NUMBER,
            rate_smoothing NUMBER
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
            current_mode TEXT, 
            aoo_id NUMBER,
            voo_id NUMBER,
            aai_id NUMBER,
            vvi_id NUMBER,
            FOREIGN KEY (aoo_id) REFERENCES aoo(id),
            FOREIGN KEY (voo_id) REFERENCES voo(id),
            FOREIGN KEY (aai_id) REFERENCES aai(id),
            FOREIGN KEY (vvi_id) REFERENCES vvi(id)
        );
    """)