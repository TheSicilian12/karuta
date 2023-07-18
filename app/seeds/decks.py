from app.models import db, Decks, environment, SCHEMA;
from sqlalchemy.sql import text;

def seed_decks():
    deck1 = Decks(
        name = 'deck 1'
    )
    deck2 = Decks(
        name = 'deck 2'
    )
    deck3 = Decks(
        name = 'deck 3'
    )
    deck4 = Decks(
        name = 'deck 4'
    )


    db.session.add(deck1)
    db.session.add(deck2)
    db.session.add(deck3)
    db.session.add(deck4)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_decks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.decks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM decks"))

    db.session.commit()
