from .. import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites', back_populates='User', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
#metodods de instacia
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
           # "is_active":
            # do not serialize the password, its a security breach
        }
    def serialize_favorites(self):
        return [favorite.serialize() for favorite in self.favorites]