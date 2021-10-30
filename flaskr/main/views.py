from flask import Blueprint, render_template

main = Blueprint("main", __name__,
                           template_folder="templates")


@main.route("/")
def hello_world():
    return render_template("main/home.html")