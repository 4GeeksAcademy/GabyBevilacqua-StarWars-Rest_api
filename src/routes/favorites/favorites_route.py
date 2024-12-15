from flask import Blueprint, jsonify, request
from models.favorites.favorites_model import Favorites
from models.user.user_model import User
from models.people.people_model import People
from models.planets.planets_model import Planets
from models import db


favorites_bp= Blueprint('favorites', __name__)

@favorites_bp.route('/people/<int:people_id>', methods=['POST'])
def add_favorite_person(people_id):
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    person = People.query.get(people_id)
    if not user or not person:
      return jsonify({'error': 'User or Person not found'}), 404
    favorites = Favorites(user_id=user.id, people_id=person.id)
    db.session.add(favorites)
    db.session.commit()
    return jsonify({'message': 'Person added to favorites'})