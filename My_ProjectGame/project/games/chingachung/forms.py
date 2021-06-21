from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class PLAY_Form(FlaskForm):
    fnum = StringField("Your choice:",validators = [DataRequired()])
    play = SubmitField("Ok")
