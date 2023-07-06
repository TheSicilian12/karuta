from app.models import db, karuta_cards, environment, SCHEMA
from sqlalchemy.sql import text
import karutaData from '../storage/Data/KarutaCardData.js'

def karuta_cards():
    # card1 = karuta_cards(
    #     english_line1 = "",
    #     english_line2 = "",
    #     english_line3 = "",
    #     english_line4 = "",
    #     english_line5 = "",
    #     english_author = "",

    #     japanese_line1 = "",
    #     japanese_line2 = "",
    #     japanese_line3 = "",
    #     japanese_line4 = "",
    #     japanese_line5 = "",
    #     japanese_author = "",

    #     romaji_line1 = "",
    #     romaji_line2 = "",
    #     romaji_line3 = "",
    #     romaji_line4 = "",
    #     romaji_line5 = "",
    #     romaji_author = "",
    # )




    db.session.add(card1)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_karuta_cards():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.karuta_cards RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM karuta_cards"))

    db.session.commit()
