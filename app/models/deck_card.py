from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from .deck_card_association import deck_card_association


class Deck_Cards(db.Model):
    __tablename__ = 'deck_cards'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    answer = db.Column(db.String, nullable=False)
    answer_long = db.Column(db.String, nullable=True)
    question = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime)

    # Foreign Keys
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))

    # Relationships
    # Many to Many
    decks = db.relationship('Decks', secondary=deck_card_association, back_populates='cards')

    def to_dict(self):
        return {
            'id': self.id,

            'answer': self.answer,
            'answer_long': self.answer_long,
            'question': self.question,
            'owner_id': self.owner_id,

            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
