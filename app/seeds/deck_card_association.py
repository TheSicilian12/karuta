from app.models import db, Deck_Cards, Decks, environment, SCHEMA;
from sqlalchemy.sql import text;

def seed_deck_cards():
    card1 = Deck_Cards(
        question = 'What is the first karuta poem in the data?',
        answer = 'Coarse the rush-mat roof',
        answer_long = 'Coarse the rush-mat roof Sheltering the harvest-hut Of the autumn rice-field; And my sleeves are growing wet With the moisture dripping through. Emperor Tenchi'
    )
    card2 = Deck_Cards(
        question='What is 2 + 2?',
        answer='4'
    )
    card3 = Deck_Cards(
        question = 'How do you play karuta?',
        answer = 'Memorize the cards and select the right one first',
    )
    card4 = Deck_Cards(
        question = 'writing systems',
        answer = 'hirgana and katakan',
        answer_long = 'hiragana, katakana, and kanji'
    )


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
def undo_deck_cards():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.deck_cards RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM deck_cards"))

    db.session.commit()
