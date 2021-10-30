from flask import Flask

try:
    from flaskr.main import main
    from flaskr.configurations import configurations
    from flaskr.projects import projects
except Exception as e:
    print(e)

app = Flask(__name__)
app.config["SECRET_KEY"] = "f6cd4f49c529716ee76d4147bad80eac"

app.register_blueprint(main)
app.register_blueprint(configurations)
app.register_blueprint(projects)


