from flaskr.util import GenPage
import mongoengine as me
from datetime import datetime

class Proj(GenPage):
    global_id = 0
    def __init__(self, name):
        super().__init__(name)
        Proj.global_id += 1
        self.id = Proj.global_id


class Project(me.Document):
    # an id field is created automatically, according to documentation
    time_created = me.DateTimeField(default=datetime.now)
    name = me.StringField(required=True)

    def __str__(self):
        return self.name