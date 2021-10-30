from flask import Blueprint, redirect, render_template, request, url_for
from .models import Config
from .forms import ConfigurationForm

configurations = Blueprint("configurations", __name__,
                           template_folder="templates")

user_configs = []

def get_config_byid(int_id):
    config_dict = {config.id:config for config in user_configs}
    return config_dict.get(int_id)


@configurations.route("/configurations")
def configurations_view():
    return render_template("configurations/configurations.html", configs=user_configs)


@configurations.route("/configuration/<int:config_id>/")
def single_config_view(config_id):
    user_config = get_config_byid(config_id)
    return render_template("configurations/single_config.html", config=user_config)


@configurations.route("/newconfiguration", methods=["GET", "POST"])
def new_configuration_view():
    form = ConfigurationForm()
    if form.validate_on_submit():
        user_configs.append(Config(form.name.data))
        return redirect(url_for('.configurations_view'))
    return render_template("configurations/new_config.html", form=form)