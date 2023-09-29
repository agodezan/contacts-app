"""define some root
"""
#
from flask import Blueprint, render_template, request, redirect, url_for
from contacts_app.db.db import get_db_connection

contact_bp = Blueprint(
    "contact_bp",
    __name__,
    url_prefix="/contact",
    template_folder="templates",
    static_folder="../static",
)


@contact_bp.route("/all")
def all():
    conn = get_db_connection()
    users_list = conn.execute("SELECT * FROM persons").fetchall()

    conn.close()

    return render_template("all_contacts.html", users_list=users_list)


@contact_bp.route("/new")
def new():
    return render_template("new_contact.html")


@contact_bp.route("/add_new", methods=["GET", "POST"])
def add_new_contact():
    username = request.form.get("username")
    emailaddress = request.form.get("emailaddress")
    whatsapp = request.form.get("whatsapp")

    conn = get_db_connection()

    conn.execute(
        "INSERT INTO persons (username, emailaddress, whatsapp) VALUES (?, ?, ?)",
        (username, emailaddress, int(whatsapp)),
    )
    conn.commit()
    conn.close()
    return redirect(url_for("home.index"))
