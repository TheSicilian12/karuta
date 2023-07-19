from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Deck_Cards

class DeckCardForm(FlaskForm):
    answer = StringField(
        'answer', validators=[DataRequired()]
    )
    answer_long = StringField(
        'answer_long'
    )
    question = StringField(
        'question', validators=[DataRequired()]
    )
    owner_id = IntegerField(
        'owner_id', validators=[DataRequired()]
    )
