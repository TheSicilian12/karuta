from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from .deck_card_association import deck_card_association
from .user_deck_association import user_deck_association

class Decks(db.Model):
    __tablename__ = 'decks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime)

    # Foreign Keys
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))

    # Relationships
    # Many to Many
    cards = db.relationship('Deck_Cards', secondary=deck_card_association, back_populates='decks')
    users = db.relationship('User', secondary=user_deck_association, back_populates='decks')

    def to_dict(self):
        return {
            'id': self.id,

            'name': self.name,
            'owner_id': self.owner_id,

            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
