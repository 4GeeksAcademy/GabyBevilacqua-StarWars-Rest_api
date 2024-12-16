from flask import Blueprint,jsonify, request
from models.planets.planets_model import Planets
from models import db

planets_bp = Blueprint('planets1',__name__)

@planets_bp.route("/", methods=["GET"])
def get_planets():
    list_planets = Planets.query.all()
    list_planets = [planets.serialize() for planets in list_planets]  
    return jsonify({"list_planets":list_planets})

@planets_bp.route("/<int:planets_id>", methods = ["GET"]) 
def get_planet(planets_id):
        planet = Planets.query(planets_id)
        return jsonify({"planet":planet.serialize()})

@planets_bp.route('/create',methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_planet = Planets(**user_data)
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({"msg":"Planet created succesfull"}),201