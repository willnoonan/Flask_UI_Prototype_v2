import mongoengine as me
from datetime import datetime


class Configuration(me.Document):
    # an id field is created automatically, according to documentation
    time_created = me.DateTimeField(default=datetime.now)
    name = me.StringField(required=True)

    def __str__(self):
        return self.name