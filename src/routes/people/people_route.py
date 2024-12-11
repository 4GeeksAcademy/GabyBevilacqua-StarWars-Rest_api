from flask import Blueprint

people_bp = Blueprint('people',__name__)

@people_bp.route("/", methods=["GET"])
def get_people():
    return "people esta funcionando", 200

@people_bp.route("/<int:people_id>", methods = ["GET"]) 
def get_character(people_id):
        return "retornando personaje", 200

#@people_bp.route("/<int:people_id", methods=["POST"])
#def get_favorites():
#    return "todos los favoritos", 200

#@people_bp.route("<int:people_id", methods=["DELETE"])
#def get_favorites():
#    return "todos los favoritos", 200