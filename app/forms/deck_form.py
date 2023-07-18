from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import Decks

class DeckForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
