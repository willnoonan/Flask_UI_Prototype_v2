from flask import Blueprint, redirect, render_template, request, url_for
from .models import Config

configurations = Blueprint("configurations", __name__,
                           template_folder="templates")

user_configs = []

def get_config_byid(int_id):
    config_dict = {config.id:config for config in user_configs}
    return config_dict.get(int_id)

@configurations.route("/test_configurations")
def test_configs_view():
    return "<h1>Test: Configurations.</h1>"

@configurations.route("/configurations")
def configurations_view():
    return render_template("configurations/configurations.html", configs=user_configs)


@configurations.route("/configuration/<int:config_id>/")
def single_config_view(config_id):
    user_config = get_config_byid(config_id)
    return render_template("configurations/single_config.html", config=user_config)

@configurations.route("/newconfiguration", methods=["POST", "GET"])
def new_configuration_view():
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            return "failure"
        user_configs.append(Config(name))
        return redirect(url_for('.configurations_view'))
    return render_template("configurations/new_config.html")