from app.models import db, Deck_Cards, Decks, environment, SCHEMA;
from sqlalchemy.sql import text;

def seed_deck_card_association():
    deck1 = Decks.query.filer(name = 'Deck 1').first()
    deck2 = Decks.query.filer(name = 'Deck 1').first()
    deck3 = Decks.query.filer(name = 'Deck 1').first()
    deck4 = Decks.query.filer(name = 'Deck 1').first()

card1 = Deck_Cards.query.filter(question = 'What is the first karuta poem in the data?').first()
card1 = Deck_Cards.query.filter(question = 'What is 2 + 2?').first()
card1 = Deck_Cards.query.filter(question = 'How do you play karuta?').first()
card1 = Deck_Cards.query.filter(question = 'Memorize the cards and select the right one first').first()

    db.session.add(card1)
    db.session.add(card2)
    db.session.add(card3)
    db.session.add(card4)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_deck_card_association():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.deck_card_association RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM deck_card_association"))

    db.session.commit()
