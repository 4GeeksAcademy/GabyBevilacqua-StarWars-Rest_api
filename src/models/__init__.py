from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user.user_model import User
from .people.people_model import People
from .planets.planets_model import Planets
from .favorites.favorites_model import Favorites