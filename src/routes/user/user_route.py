from flask import Blueprint, request, jsonify
from models import db, User

user_bp = Blueprint('user1', __name__)

@user_bp.route("/", methods=["GET"])
def base_function():
    return "esta funcionando", 200

@user_bp.route("/user/get", methods=["GET"])
def get_list_user():
   list_user = User.query.all()
   list_user = [user.serialize() for user in list_user]  
   return jsonify({"list_user":list_user})

@user_bp.route("/user/create", methods=["POST"])
def create_user():  
    user_data = request.get_json()
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()
    return "usuario creado", 201
