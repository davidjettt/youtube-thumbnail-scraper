from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ChannelForm(FlaskForm):
    channel_url = StringField('channel_url')
    submit = SubmitField('submit')
