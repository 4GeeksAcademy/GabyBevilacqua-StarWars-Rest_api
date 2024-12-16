from flask import Blueprint, jsonify, request
from models.people.people_model import People
from models import db

people_bp = Blueprint('people1',__name__)

@people_bp.route("/", methods=["GET"])
def get_people():
    list_people = People.query.all()
    list_people = [people.serialize() for people in list_people] 
    return jsonify({"list_people":list_people})

@people_bp.route("/<int:people_id>", methods = ["GET"]) 
def get_character(people_id):
    person = People.query(people_id)
    return jsonify({"person":person.serialize()})

@people_bp.route('/create',methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_people = People(**user_data)
    db.session.add(new_people)
    db.session.commit()
    return jsonify({"msg":"People created succesfull"}),201
