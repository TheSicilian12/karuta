from flask import Blueprint, jsonify, session, request
from app.models import User, Decks, user_deck_association, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import karuta_form
import random

deck_routes = Blueprint('deck', __name__)



# GET all your decks
@deck_routes.route('/user/<int:user_id>')
@login_required
def get_your_decks(user_id):
    """
    GET all decks for the current user
    """
    print('---------------------Get current user decks----------------------')
    # Owned decks (this needs more work)
    # Decks subscribed to (check)

    if current_user.id != user_id:
        return {'error': 'Invalid route'}

    user_decks = current_user.decks
    response = [deck.to_dict() for deck in user_decks]
    # print('---------------------user_decks: ', user_decks)
    return response

# GET a specific deck
@deck_routes.route('/<int:deck_id>')
@login_required
def get_one_deck(deck_id):
    """
    GET one deck belonging to the current user
    """
    print('--------------------Get one deck current user--------------------')

    deck = Decks.query.get(deck_id)

    # check if user is subscribed to the deck
    # check if the user is the owner of the deck

    # all users subscribed to this deck
    deck_users = deck.users

    # what about invalid responses?
    # checking for the current user to be in the subscribed list
    user = [user.to_dict() for user in deck_users if user.id == current_user.id]

    # checking  if there is exactly 1 user in the list.
    if len(user) != 1:
        return {'error': 'Invalid route'}

    return deck.to_dict()
