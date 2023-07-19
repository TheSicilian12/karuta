from app.models import db, User, Decks, user_deck_association, environment, SCHEMA;
from sqlalchemy.sql import text;

def seed_user_deck_association():
    deck1 = Decks.query.get(1)
    deck2 = Decks.query.get(2)
    deck3 = Decks.query.get(3)
    deck4 = Decks.query.get(4)


    user1 = User.query.get(1)
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    user4 = User.query.get(4)


    deck1.users.append(user1)
    deck1.users.append(user2)
    deck1.users.append(user3)
    deck1.users.append(user4)

    deck2.users.append(user1)
    deck2.users.append(user2)

    deck3.users.append(user3)
    
    deck4.users.append(user4)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_user_deck_association():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_deck_association RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_deck_association"))

    db.session.commit()
