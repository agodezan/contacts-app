"""define some code for home
"""
from flask import Blueprint, render_template


home_bp = Blueprint(
    "home", __name__, template_folder="templates", static_folder="../static"
)


# need to use now home_bp instead of app for route annotations
@home_bp.route("/")
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template("home.html")
