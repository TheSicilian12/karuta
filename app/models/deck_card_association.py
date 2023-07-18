from .db import db

deck_card_association = db.Table('deck_card_association',
    db.Column('deck_id', db.Integer, db.ForeignKey('decks.id'), primary_key=True),
    db.Column('deck_card_id', db.Integer, db.ForeignKey('deck_cards.id'), primary_key=True)
)
