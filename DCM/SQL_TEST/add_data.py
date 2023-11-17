import sqlite3

connect = sqlite3.connect('DCM\\SQL_TEST\\data.db') 
cursor = connect.cursor()

cursor.execute("""
    INSERT INTO aoo VALUES (
        1, 60, 120, 3.5, 0.4
    );
""")

cursor.execute("""
    INSERT INTO voo VALUES (
        1, 60, 120, 3.5, 0.4
    );
""")

cursor.execute("""
    INSERT INTO users VALUES (
        1, 'admin', 'admin', 'aoo', 1, 1, 0, 0
    );
""")

connect.commit()