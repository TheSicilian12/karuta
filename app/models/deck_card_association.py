from .db import db, environment, add_prefix_for_prod, SCHEMA

deck_card_association = db.Table('deck_card_association',
    db.Model.metadata,
    db.Column('deck_id', db.Integer, db.ForeignKey(add_prefix_for_prod('decks.id')), primary_key=True),
    db.Column('deck_card_id', db.Integer, db.ForeignKey(add_prefix_for_prod('deck_cards.id')), primary_key=True)
)
if environment == "production":
    deck_card_association.schema = SCHEMA
