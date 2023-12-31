import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO persons (username, emailaddress, whatsapp) VALUES (?, ?, ?)",
            ('Agostina De Zan', 'agodezan@gmail.com', 34300022555)
            )

cur.execute("INSERT INTO persons (username, emailaddress, whatsapp) VALUES (?, ?, ?)",
            ('Ezequiel Tejerina', 'ezequieltejerina@gmail.com', 34100002255)
            )

connection.commit()
connection.close()
