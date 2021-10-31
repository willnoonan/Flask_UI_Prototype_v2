from flaskr.util import GenPage
import mongoengine as me
from datetime import datetime

class Config(GenPage):
    global_id = 0
    def __init__(self, name):
        super().__init__(name)
        Config.global_id += 1
        self.id = Config.global_id

class Configuration(me.Document):
    # an id field is created automatically, according to documentation
    time_created = me.DateTimeField(default=datetime.now)
    name = me.StringField(required=True)

    def __str__(self):
        return self.name