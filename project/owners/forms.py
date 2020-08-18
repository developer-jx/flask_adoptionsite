from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of Owner: ")
    pup_id = IntegerField("ID of Puppy: ")
    submit = SubmitField("Submit")

class DelForm(FlaskForm):
    owner_id = IntegerField("ID of Owner: ")
    submit = SubmitField("Delete")