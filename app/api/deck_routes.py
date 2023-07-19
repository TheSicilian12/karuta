from flask import Blueprint, jsonify, session, request
from app.models import User, Decks, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import karuta_form
import random

deck_routes = Blueprint('deck', __name__)


# GET all karuta cards
@deck_routes.route('/')
def get_all_decks():
    '''
    GET all decks
    '''
    print("---------------------------get all decks---------------------------------")
    all_decks = Decks.query.all()
    # print("---------------------all_decks: ", all_decks)

    response = [deck.to_dict() for deck in all_decks]

    return {'decks': response}
