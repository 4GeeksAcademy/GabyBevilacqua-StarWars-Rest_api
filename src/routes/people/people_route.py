from flask import Blueprint
from models.people.people_model import People

people_bp = Blueprint('people',__name__)

@people_bp.route("/", methods=["GET"])
def get_people():
    people = People.query.all()
    return "people esta funcionando", 200
#   return jsonify([person.name for person in people])

@people_bp.route("/<int:people_id>", methods = ["GET"]) 
def get_character(people_id):
        person = People.query.get(people_id)
        return "retornando personaje", 200

#@people_bp.route("/<int:people_id", methods=["POST"])
#def get_favorites():
#    return "todos los favoritos", 200

#@people_bp.route("<int:people_id", methods=["DELETE"])
#def get_favorites():
#    return "todos los favoritos", 200