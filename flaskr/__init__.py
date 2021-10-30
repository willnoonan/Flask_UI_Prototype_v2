from flask import Flask, redirect, render_template, request
# from configurations import configurations
try:
    from flaskr.main import main
    from flaskr.configurations import configurations
    from flaskr.projects import projects

except Exception as e:
    print(e)

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(configurations)
app.register_blueprint(projects)


