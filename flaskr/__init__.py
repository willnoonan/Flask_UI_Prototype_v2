from flask import Flask
from mongoengine import connect

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

#--------------
# mongodb setup
#--------------
# 1a. Install mongodb community edition following directions on their website
# 1b. Install mongodb Compass tool (optional)
# 2. Run in terminal to start server: brew services start mongodb-community@5.0
# 3. Connect to mongodb:
connect()
# 4. Run Compass tool, click connect button (optional)
# To stop server: brew services stop mongodb-community@5.0

