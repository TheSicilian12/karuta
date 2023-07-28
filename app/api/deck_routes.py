from flask import Blueprint, jsonify, session, request
from app.models import User, Decks, user_deck_association, deck_card_association, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import karuta_form, DeckForm
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
    response = [deck.to_dict() for deck in user_decks if deck.to_dict()['owner_id'] == current_user.id]
    print('---------------------user_decks: ', response)
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

    # all cards associated with this deck
    cards_association = deck.cards

    # what about invalid responses?
    # checking for the current user to be in the subscribed list
    user = [user.to_dict() for user in deck_users if user.id == current_user.id]

    # checking  if there is exactly 1 user in the list.
    if len(user) != 1:
        return {'error': 'Invalid route'}

    # preparing cards
    cards = [card.to_dict() for card in cards_association]

    response = {}
    response['deck'] = deck.to_dict()
    response['cards'] = cards

    return response


# POST a deck
@deck_routes.route('/post', methods=['POST'])
@login_required
def post_deck():
    """
    POST a deck
    """
    print('--------------------POST a deck--------------------')
    form = DeckForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    user = User.query.get(current_user.id)

    if form.validate_on_submit():
        data = form.data

        if current_user.id != data['owner_id']:
            return {'message': 'Invalid route'}

        new_deck = Decks(
            name = data['name'],
            owner_id = data['owner_id']
        )
        db.session.add(new_deck)
        user.decks.append(new_deck)
        db.session.commit()

        print('--------------------------new_deck: ', new_deck.to_dict())
        return {'deck': new_deck.to_dict()}
    else:
        return {'error': 'Invlaid route'}
