import sqlite3
from loader.loader import load_soliders_from_csv

DB_NAME = 'initializeScheme.db'


def get_db_connection():

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def setup_database(csv_filename="../hayal_300_no_status.csv"):

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS soliders (
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

    cursor = conn.execute("SELECT COUNT(*) FROM soliders")
    if cursor.fetchone()[0] == 0:
        print("The table is empty, loading from csv")
        initial_soliders = load_soliders_from_csv(csv_filename)  # הפונקציה משלב 1

        for s in initial_soliders:
            conn.execute("""
                INSERT INTO soliders (personal_number, f_name, l_name, gender, city, distance, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (s.personal_number, s.f_name, s.l_name, s.gender, s.city, s.distance, s.status))

        conn.commit()
        print(f" {len(initial_soliders)} items loaded")

    conn.close()


setup_database()