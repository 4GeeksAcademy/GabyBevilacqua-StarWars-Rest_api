from .. import db

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    user = db.relationship('User', back_populates='favorites')
    people = db.relationship('People', back_populates='favorites')
    planets = db.relationship('Planets', back_populates='favorites')

    def __repr__(self):
        return '<Favourites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.serialize() if self.user else None,  
            "people": self.people.serialize() if self.people else None, 
            "planets": self.planets.serialize() if self.planets else None  
        }