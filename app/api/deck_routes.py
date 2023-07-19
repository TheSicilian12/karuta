from flask import Blueprint, jsonify, session, request
from app.models import User, Decks, user_deck_association, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import karuta_form
import random

deck_routes = Blueprint('deck', __name__)



# GET all your decks
@deck_routes.route('/<int:user_id>')
@login_required
def get_your_decks(user_id):
    """
    GET all decks for the current user
    """
    print('---------------------Get current user decks----------------------')
    # Owned decks
    # Decks subscribed to

    if current_user.id != user_id:
        return {'error': 'Invalid route'}

    user_decks = current_user.decks
    response = [deck.to_dict() for deck in user_decks]
    # print('---------------------user_decks: ', user_decks)
    return response
