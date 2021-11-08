from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=30)])
    submit = SubmitField("Submit")