import sqlite3
from loader.loader import load_soldiers_from_csv, load_soldiers_from_csv

DB_NAME = 'initializeScheme.db'


def get_db_connection():

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def setup_database_soldier(csv_filename="../hayal_300_no_status.csv"):

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS soldiers (
            personal_number INTEGER PRIMARY KEY,
            f_name TEXT NOT NULL,
            l_name TEXT NOT NULL,
            gender TEXT NOT NULL,
            city TEXT NOT NULL,
            distance INTEGER NOT NULL,
            status TEXT NULL
        )
    """)
    conn.commit()

    cursor = conn.execute("SELECT COUNT(*) FROM soldiers")
    if cursor.fetchone()[0] == 0:
        print("The table is empty, loading from csv")
        initial_soldiers = load_soldiers_from_csv(csv_filename)

        for s in initial_soldiers:
            conn.execute("""
                INSERT INTO soldiers (personal_number, f_name, l_name, gender, city, distance, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (s.personal_number, s.f_name, s.l_name, s.gender, s.city, s.distance, s.status))

        conn.commit()
        print(f" {len(initial_soldiers)} items loaded")

    conn.close()


setup_database_soldier()




def setup_database_house(data):

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS house (
            id_house INTEGER PRIMARY KEY,
            num_room int NOT NULL,
            personal_number int NOT NULL
            )
            """)
    conn.commit()

    conn.commit()

    cursor = conn.execute("SELECT COUNT(*) FROM house")
    if cursor.fetchone()[0] == 0:
        print("The table is empty, loading from data")
        initial_houses = load_soldiers_from_csv(data)

        for s in initial_houses:
            conn.execute("""
                    INSERT INTO house (id_house, num_room, personal_number)
                    VALUES (?, ?, ?)
                """, (s.id_house, s.num_room, s.personal_number))

        conn.commit()
        print(f" {len(initial_houses)} items loaded")

    conn.close()

setup_database_house()