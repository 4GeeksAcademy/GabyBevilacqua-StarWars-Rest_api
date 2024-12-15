from flask import Blueprint,jsonify
from models.planets.planets_model import Planets

planets_bp = Blueprint('planets',__name__)

@planets_bp.route("/get", methods=["GET"])
def get_planets():
    list_planets = Planets.query.all()
    list_planets = [planets.serialize() for planets in list_planets]  
    return jsonify({"list_planets":list_planets})

@planets_bp.route("/get/<int:planets_id>", methods = ["GET"]) 
def get_planet(planets_id):
        planet = Planets.query(planets_id)
        return jsonify({"planet":planet.serialize()})
