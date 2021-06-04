from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class PLAY_Form1(FlaskForm):
    play1 = SubmitField("OK")
    fnum = StringField("write a letter:",validators = [DataRequired()])
