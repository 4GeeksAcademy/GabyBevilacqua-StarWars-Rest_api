from flask import Blueprint

user_bp = Blueprint('user11', __name__)

@user_bp.route("/", methods=["GET"])
def base_function():
    return "esta funcionando", 200

@user_bp.route("/create", methods=["GET"])
def create_user():
    return "usuario creado", 201

@user_bp.route("/favorites", methods=["GET"])
def get_favorites():
    return "todos los favoritos", 200
