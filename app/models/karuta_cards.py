from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class karuta_cards(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    english_line1 = db.Column(db.String(1000))
    english_line2 = db.Column(db.String(1000))
    english_line3 = db.Column(db.String(1000))
    english_line4 = db.Column(db.String(1000))
    english_line5 = db.Column(db.String(1000))
    english_author = db.Column(db.String(1000))

    japanese_line1 = db.Column(db.String(1000))
    japanese_line2 = db.Column(db.String(1000))
    japanese_line3 = db.Column(db.String(1000))
    japanese_line4 = db.Column(db.String(1000))
    japanese_line5 = db.Column(db.String(1000))
    japanese_author = db.Column(db.String(1000))

    romaji_line1 = db.Column(db.String(1000))
    romaji_line2 = db.Column(db.String(1000))
    romaji_line3 = db.Column(db.String(1000))
    romaji_line4 = db.Column(db.String(1000))
    romaji_line5 = db.Column(db.String(1000))
    romaji_author = db.Column(db.String(1000))

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime)

    # Foreign Keys

    # Relationships

    def to_dict(self):
        return {
            'id': self.id,

            'english_line1': self.english_line1,
            'english_line2': self.english_line2,
            'english_line3': self.english_line3,
            'english_line4': self.english_line4,
            'english_line5': self.english_line5,
            'english_author': self.english_author,

            'japanese_line1': self.japanese_line1,
            'japanese_line2': self.japanese_line2,
            'japanese_line3': self.japanese_line3,
            'japanese_line4': self.japanese_line4,
            'japanese_line5': self.japanese_line5,
            'japanese_author': self.japanese_author,

            'romaji_line1': self.romaji_line1,
            'romaji_line2': self.romaji_line2,
            'romaji_line3': self.romaji_line3,
            'romaji_line4': self.romaji_line4,
            'romaji_line5': self.romaji_line5,
            'romaji_author': self.romaji_author,


            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
