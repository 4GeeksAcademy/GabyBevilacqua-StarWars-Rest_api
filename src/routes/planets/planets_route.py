from flask import Blueprint
from models.planets.planets_model import Planets

planets_bp = Blueprint('planets',__name__)

@planets_bp.route("/", methods=["GET"])
def get_planets():
    return "planetas esta funcionando", 200

@planets_bp.route("/<int:planets_id>", methods = ["GET"]) 
def get_planet(planets_id):
        return "retornando planeta", 200