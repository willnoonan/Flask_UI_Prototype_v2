from flask import Blueprint, redirect, render_template, request, url_for
from .models import Config
from .forms import ConfigurationForm
from .models import Configuration
from bson.objectid import ObjectId

configurations = Blueprint("configurations", __name__,
                           template_folder="templates")


@configurations.route("/configurations")
def configurations_view():
    configs = Configuration.objects()
    return render_template("configurations/configurations.html", configs=configs)


@configurations.route("/configuration/<string:config_id>/")
def single_config_view(config_id):
    config = Configuration.objects.get(id=config_id)
    return render_template("configurations/single_config.html", config=config)


@configurations.route("/newconfiguration", methods=["GET", "POST"])
def new_configuration_view():
    form = ConfigurationForm()
    if form.validate_on_submit():
        config = Configuration()
        config.name = form.name.data
        config.save()
        return redirect(url_for('.configurations_view'))
    return render_template("configurations/new_config.html", form=form)