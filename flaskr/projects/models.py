import mongoengine as me
from datetime import datetime
from flaskr.configurations.models import Configuration

class Project(me.Document):
    # an id field is created automatically, according to documentation
    time_created = me.DateTimeField(default=datetime.now)
    name = me.StringField(required=True)
    config = me.ReferenceField(Configuration, reverse_delete_rule=me.DENY)

    def __str__(self):
        return self.name