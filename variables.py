from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

global funny 
funny = "funny"

class ScoutingForm(FlaskForm):
    scouterInitials = StringField("Scouter Initials")
    teamNumber = StringField("Team Number")
    submit = SubmitField("Submit")

'''
class Counters():
    def __init__(self):
        autoNotes = 0
'''