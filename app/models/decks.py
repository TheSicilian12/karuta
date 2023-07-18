from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Decks(db.Model):
    __tablename__ = 'decks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    answer=db.Column(db.String, nullable=False)
    answer_long=db.Column(db.String, nullable=True)
    question=db.Columb(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime)

    # Foreign Keys

    # Relationships

    def to_dict(self):
        return {
            'id': self.id,
            'answer': self.answer,
            'answer_long': self.answer_long,
            'question': self.question,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
