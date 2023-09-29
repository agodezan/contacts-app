import sqlite3

connection = sqlite3.connect("database.db")


def db_init():
    """_summary_"""
    with open("contacts_app/db/schema.sql") as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    cur.execute(
        "INSERT INTO persons (username, emailaddress, whatsapp) VALUES (?, ?, ?)",
        ("Agostina De Zan", "agodezan@gmail.com", 34300022555),
    )
    cur.execute(
        "INSERT INTO persons (username, emailaddress, whatsapp) VALUES (?, ?, ?)",
        ("Ezequiel Tejerina", "ezequieltejerina@gmail.com", 34100002255),
    )
    connection.commit()
    connection.close()


def get_db_connection():
    """_summary_

    Returns:
        _type_: _description_
    """
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn
