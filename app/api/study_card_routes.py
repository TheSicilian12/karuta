from flask import Blueprint, jsonify, session, request
from app.models import User, Decks, Deck_Cards, user_deck_association, deck_card_association, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import DeckCardForm
import random

study_card_routes = Blueprint('study_cards', __name__)


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
