from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    add_note = StringField('Add Note', validators=[DataRequired()])
    submit = SubmitField('Submit')