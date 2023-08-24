from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# users_list = [{'username': 'Pepito Flores', 'emailaddress': 'pepito@gmail.com', 'whatsapp': '3434042225'}, {'username': 'Agostina De zan', 'emailaddress': 'agodezan@gmail.com', 'whatsapp': '3434042861'}]

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/all')
def all():
    conn = get_db_connection()
    users_list = conn.execute('SELECT * FROM persons').fetchall()
    conn.close()

    return render_template("all_contacts.html", users_list=users_list)

@app.route('/new')
def new():
    return render_template("new_contact.html")

@app.route("/add_new", methods=['GET', 'POST'])
def add_new_contact():
    username = request.form.get('username')
    emailaddress = request.form.get('emailaddress')
    whatsapp = request.form.get('whatsapp')

    conn = get_db_connection()

    conn.execute("INSERT INTO persons (username, emailaddress, whatsapp) VALUES (?, ?, ?)",
            (username, emailaddress, int(whatsapp))
            )
    conn.commit()
    conn.close()
    return render_template("home.html")

if __name__ == '__main__':
    app.run()

