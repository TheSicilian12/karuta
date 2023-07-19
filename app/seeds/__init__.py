from flask.cli import AppGroup
from .users import seed_users, undo_users
from .karuta_cards import seed_karuta_cards, undo_karuta_cards
from .deck_cards import seed_deck_cards, undo_deck_cards
from .decks import seed_decks, undo_decks
from .deck_card_association import seed_deck_card_association, undo_deck_card_association
from .user_deck_association import seed_user_deck_association, undo_user_deck_association


from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_user_deck_association()
        undo_deck_card_association()
        undo_decks()
        undo_deck_cards()
        undo_karuta_cards()
        undo_users()
    seed_users()
    seed_karuta_cards()
    seed_deck_cards()
    seed_decks()
    seed_deck_card_association()
    seed_user_deck_association()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_user_deck_association()
    undo_deck_card_association()
    undo_decks()
    undo_deck_cards()
    undo_karuta_cards()
    undo_users()
    # Add other undo functions here
