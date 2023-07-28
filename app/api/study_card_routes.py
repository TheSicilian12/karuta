from flask import Blueprint, jsonify, session, request
from app.models import User, Decks, Deck_Cards, user_deck_association, deck_card_association, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import DeckCardForm

import random

study_card_routes = Blueprint('study_cards', __name__)

# GET a users cards
@study_card_routes.route('/users')
@login_required
def get_users_cards():
    """
    GET a users cards
    """
    print("---------------------------get a users cards-------------------------")

    cards = Deck_Cards.query.filter(Deck_Cards.owner_id == current_user.id).all()

    # decks_association = cards[0].decks

    # cardsAddDeck = [deck.to_dict() for deck in decks_association]
    # print("----------------add cards deck: ", cardsAddDeck)
    # cardsResponse = [card.to_dict() for card in cards]

    cardsResponse = []
    for card in cards:
        # print('-------------------------card: ', card)
        decks = card.decks
        # cardDecks = [deck.to_dict()["id"] for deck in decks if deck.to_dict()["owner_id"] == current_user.id]

        # This may end up being a problem. As of now this is needed and filtering by onwer id doesn't work
        cardDecks = [deck.to_dict()["id"] for deck in decks]

        # print('---------------------cardDecks: ', cardDecks)

        cardUpdate = card.to_dict()
        cardUpdate["decks"] = cardDecks
        cardsResponse.append(cardUpdate)

    return cardsResponse


# EDIT a study card
@study_card_routes.route('/<int:cardId>', methods=['PUT'])
@login_required
def edit_study_card(cardId):
    """
    EDIT a study card
    """
    print('---------------------edit a study card-----------------')

    card = Deck_Cards.query.get(cardId)

    if not card:
        return {'error': 'not a valid route'}

    owner_id = (card.to_dict())["owner_id"]

    if owner_id != current_user.id:
        return {'error': 'not a valid route'}

    form = DeckCardForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        print('------------------form: ', form.data)
        card.answer = form.data["answer"]
        card.answer_long = form.data["answer_long"]
        card.question = form.data["question"]
        card.owner_id = form.data["owner_id"]
        db.session.commit()
        return {"card": card.to_dict()}
    else:
        return {"error": form.errors}

# POST a study card
@study_card_routes.route('/post', methods=['POST'])
@login_required
def post_study_card():
    """
    POST a study card
    """
    print('------------------------post a study card-------------------------')

    form = DeckCardForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    # print('------------form validate: ', form.validate_on_submit())
    # print('--------------------form: ', form.data)

    if form.validate_on_submit():
        data = form.data
        new_card = Deck_Cards(
            answer = data['answer'],
            answer_long = data['answer_long'],
            question = data['question'],
            owner_id = data['owner_id']
        )
        db.session.commit()
        db.session.add(new_card)
        db.session.commit()
        print('----------------new card: ', new_card.to_dict())
        return {'card': new_card.to_dict()}
    else:
        return {'error': 'not a valid route'}


# PUT / ASSOCIATE a card and a deck
@study_card_routes.route('/associate/card/<int:cardId>/deck/<int:deckId>', methods=['PUT'])
@login_required
def associate_card_deck(cardId, deckId):
    """
    PUT / ASSOCIATE a card and a deck
    """
    print('------------------------Put / associate a card and a deck-----------------------')
    deck = Decks.query.get(deckId)
    card = Deck_Cards.query.get(cardId)

    if deck.owner_id != current_user.id:
        return {'error': 'not a valid rotue'}

    if card.owner_id != current_user.id:
        return {'error': 'not a valid route'}

    form = DeckCardForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    print('----------------------form validate associate: ', form.validate_on_submit())

    if form.validate_on_submit():
        print('------------------form: ', form.data)
        # card.answer = form.data["answer"]
        # card.answer_long = form.data["answer_long"]
        # card.question = form.data["question"]
        # card.owner_id = form.data["owner_id"]

        # this doesn't work: AttributeError: 'dict' object has no attribute 'decks'
        # card.to_dict().decks.append(deckId)
        deck.cards.append(card)
        db.session.commit()
        return {'message': 'Card associated'}
    else:
        return {"error": form.errors}


# DELETE / DISASSOCIATE a card from a deck
@study_card_routes.route('/associate/card/<int:cardId>/deck/<int:deckId>', methods=['DELETE'])
@login_required
def disassociate_card_deck(cardId, deckId):
    """
    DELETE / DISASSOCIATE a card from a deck
    """
    print('------------------------Delete / disassociate a card from a deck-----------------------')
    deck = Decks.query.get(deckId)
    card = Deck_Cards.query.get(cardId)

    if deck.owner_id != current_user.id:
        return {'error': 'not a valid rotue'}

    if card.owner_id != current_user.id:
        return {'error': 'not a valid route'}

    deck.cards.remove(card)

    db.session.commit()

    return {'message': 'Card successfully removed'}
