from flask import Blueprint, redirect, render_template, request, url_for
from .models import Config
from .forms import ConfigurationForm
from .models import Configuration

configurations = Blueprint("configurations", __name__,
                           template_folder="templates")

user_configs = []

def get_config_byid(int_id):
    config_dict = {config.id:config for config in user_configs}
    return config_dict.get(int_id)

# The following is the link I had to cut out of configurations.html to test use of Configuration model:
# <a href="{{ url_for('configurations.single_config_view', config_id=config.id) }}">{{ config }}</a>
@configurations.route("/configurations")
def configurations_view():
    configs = Configuration.objects()
    return render_template("configurations/configurations.html", configs=configs)


@configurations.route("/configuration/<int:config_id>/")
def single_config_view(config_id):
    user_config = get_config_byid(config_id)
    return render_template("configurations/single_config.html", config=user_config)

@configurations.route("/newconfiguration", methods=["GET", "POST"])
def new_configuration_view():
    form = ConfigurationForm()
    if form.validate_on_submit():
        config = Configuration()
        config.name = form.name.data
        config.save()
        # user_configs.append(Config(form.name.data))
        return redirect(url_for('.configurations_view'))
    return render_template("configurations/new_config.html", form=form)