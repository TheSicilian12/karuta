from app.models import db, Deck_Cards, Decks, deck_card_association, environment, SCHEMA;
from sqlalchemy.sql import text;

def seed_deck_card_association():
    deck1 = Decks.query.get(1)
    deck2 = Decks.query.get(2)
    deck3 = Decks.query.get(3)
    deck4 = Decks.query.get(4)


    card1 = Deck_Cards.query.get(1)
    card2 = Deck_Cards.query.get(2)
    card3 = Deck_Cards.query.get(3)
    card4 = Deck_Cards.query.get(4)


    deck1.cards.append(card1)
    deck1.cards.append(card2)
    deck1.cards.append(card3)
    deck1.cards.append(card4)

    deck2.cards.append(card1)
    deck2.cards.append(card2)

    deck3.cards.append(card3)

    deck4.cards.append(card4)

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
