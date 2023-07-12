from flask import Blueprint, jsonify, session, request
from app.models import User, karuta_cards, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import karuta_form

karuta_routes = Blueprint('karuta', __name__)


# GET all karuta cards
@karuta_routes.route('/')
def get_all_karuta_cards():
    '''
    GET all karuta cards
    '''
    print("---------------------------get all karuta cards---------------------------------")
    all_cards = karuta_cards.query.all()
    print("------------------------all_Cards: ", all_cards[0].to_dict())

    response = [card.to_dict() for card in all_cards]

    return {'cards': response}


#GET one karuta card
@karuta_routes.route('/<int:cardId>')
def get_one_karuta_card(cardId):
    '''
    GET one karuta card
    '''
    print("---------------------------get one card-------------------------")
    one_card = karuta_cards.query.filter(cardId == karuta_cards.id).first()
    print("-------------one_card: ", one_card.to_dict())
    return [one_card.to_dict()]
