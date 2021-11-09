from flask import Blueprint, render_template, request, redirect, url_for
from .models import Proj
from .models import Project
from .forms import ProjectForm


projects = Blueprint("projects", __name__,
                     template_folder="templates")

#TODO replace use of user_projects with mongodb
user_projects = []

def get_project_byid(int_id):
    proj_dict = {proj.id:proj for proj in user_projects}
    return proj_dict.get(int_id)


@projects.route("/projects")
def projects_view():
    projs = Project.objects()
    return render_template("projects/projects.html", projects=projs)


@projects.route("/project/<string:project_id>")
def single_project_view(project_id):
    proj = Project.objects.get(id=project_id)
    return render_template("projects/single_project.html", project=proj)


@projects.route("/newproject", methods=["GET", "POST"])
def new_project_view():
    form = ProjectForm()
    if form.validate_on_submit():
        proj = Project()
        proj.name = form.name.data
        proj.save()
        return redirect(url_for(".projects_view"))
    return render_template("projects/new_project.html", form=form)