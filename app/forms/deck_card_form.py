from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import Deck_Cards

class DeckCard(FlaskForm):
    answer = StringField(
        'answer', validators=[DataRequired()]
    )
    answer_long = StringField(
        'answer_long'
    )
    question = StringField(
        'question', validators=[DataRequired()]
    )
