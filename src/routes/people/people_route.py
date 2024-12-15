from flask import Blueprint, jsonify
from models.people.people_model import People

people_bp = Blueprint('people',__name__)

@people_bp.route("/get", methods=["GET"])
def get_people():
    list_people = People.query.all()
    list_people = [people.serialize() for people in list_people] 
    return jsonify({"list_people":list_people})

@people_bp.route("/get/<int:people_id>", methods = ["GET"]) 
def get_character(people_id):
        person = People.query(people_id)
        return jsonify({"person":person.serialize()})

