from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import karuta_cards

class karutaForm(FlaskForm):
    english_line1 = StringField(
        'english_line1', validators=[DataRequired()]
        )
    english_line2 = StringField(
        'english_line2', validators=[DataRequired()]
        )
    english_line3 = StringField(
        'english_line3', validators=[DataRequired()]
        )
    english_line4 = StringField(
        'english_line4', validators=[DataRequired()]
        )
    english_line5 = StringField(
        'english_line5', validators=[DataRequired()]
        )
    english_author = StringField(
        'english_line6', validators=[DataRequired()]
        )
