from flask import Blueprint, jsonify, session, request
from app.models import User, Decks, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import karuta_form
import random

deck_routes = Blueprint('deck', __name__)



# GET all your decks
@deck_routes.route('/')
@login_required
def get_your_decks()
