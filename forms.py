from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

# AddPuppyForm, DelPuppyForm, AddOwnerForm, DelOwnerForm

class AddPuppyForm(FlaskForm):
    name = StringField("Name of Puppy: ")
    submit = SubmitField("Submit")

class DelPuppyForm(FlaskForm):
    pup_id = IntegerField("ID of Puppy: ")
    submit = SubmitField("Delete")

class AddOwnerForm(FlaskForm):
    name = StringField("Name of Owner: ")
    pup_id = IntegerField("ID of Puppy: ")
    submit = SubmitField("Submit")

class DelOwnerForm(FlaskForm):
    owner_id = IntegerField("ID of Owner: ")
    submit = SubmitField("Delete")