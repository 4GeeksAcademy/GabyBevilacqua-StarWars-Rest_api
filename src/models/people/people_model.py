from .. import db


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(900), nullable=False)
    eye_color = db.Column(db.String(60), nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites', back_populates='people')


    def __repr__(self):
        return '<People %r>' % self.name
    
#metodods de instacia
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "description": self.description,
            "eye_color": self.eye_color
            # do not serialize the password, its a security breach
        }