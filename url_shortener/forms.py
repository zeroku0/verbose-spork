from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired


class ShortForm(FlaskForm):

    url = URLField("Long URL", validators=[DataRequired()])
    submit = SubmitField("Shorten!")


class ReportForm(FlaskForm):

    surl = URLField()
    submit = SubmitField("Go to home!")
