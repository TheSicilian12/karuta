from .db import db, environment, add_prefix_for_prod, SCHEMA

user_deck_association = db.Table('user_deck_association',
    db.Model.metadata,
    db.Column('deck_id', db.Integer, db.ForeignKey(add_prefix_for_prod('decks.id')), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True)
)
if environment == "production":
    user_deck_association.schema = SCHEMA
