from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of Puppy: ")
    submit = SubmitField("Submit")

class DelForm(FlaskForm):
    pup_id = IntegerField("ID of Puppy: ")
    submit = SubmitField("Delete")