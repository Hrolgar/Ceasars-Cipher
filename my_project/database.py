import sqlite3


def save_data(app_name: str, password: str, input_shift: int):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()

    # Create table - Passwords if it doesn't exist
    c.execute('CREATE TABLE IF NOT EXISTS Passwords(AppName text, Password text, Shift real)')

    c.execute("INSERT INTO Passwords VALUES (?, ?, ?)", (app_name, password, input_shift))
    conn.commit()
    conn.close()


