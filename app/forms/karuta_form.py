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
        'english_author', validators=[DataRequired()]
        )

    japanese_line1 = StringField(
        'japanese_line1', validators=[DataRequired()]
        )
    japanese_line2 = StringField(
        'japanese_line2', validators=[DataRequired()]
        )
    japanese_line3 = StringField(
        'japanese_line3', validators=[DataRequired()]
        )
    japanese_line4 = StringField(
        'japanese_line4', validators=[DataRequired()]
        )
    japanese_line5 = StringField(
        'japanese_line5', validators=[DataRequired()]
        )
    japanese_author = StringField(
        'japanese_author', validators=[DataRequired()]
        )

    romaji_line1 = StringField(
        'romaji_line1', validators=[DataRequired()]
        )
    romaji_line2 = StringField(
        'romaji_line2', validators=[DataRequired()]
        )
    romaji_line3 = StringField(
        'romaji_line3', validators=[DataRequired()]
        )
    romaji_line4 = StringField(
        'romaji_line4', validators=[DataRequired()]
        )
    romaji_line5 = StringField(
        'romaji_line5', validators=[DataRequired()]
        )
    romaji_author = StringField(
        'romaji_author', validators=[DataRequired()]
        )
