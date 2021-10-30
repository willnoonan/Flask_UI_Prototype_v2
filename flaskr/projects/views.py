from flask import Blueprint, render_template, request, redirect, url_for
from .models import Proj

projects = Blueprint("projects", __name__,
                     template_folder="templates")


user_projects = []

def get_project_byid(int_id):
    proj_dict = {proj.id:proj for proj in user_projects}
    return proj_dict.get(int_id)


@projects.route("/projects")
def projects_view():
    return render_template("projects/projects.html", projects=user_projects)


@projects.route("/project/<int:project_id>")
def single_project_view(project_id):
    user_project = get_project_byid(project_id)
    return render_template("projects/single_project.html", project=user_project)


@projects.route("/newproject", methods=["POST", "GET"])
def new_project_view():
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            return "failure"
        user_projects.append(Proj(name))
        return redirect(url_for(".projects_view"))
    return render_template("projects/new_project.html")