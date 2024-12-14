from .. import db


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
   # user = db.relationship('User', back_populates='favorites')
   # people = db.relationship('People', back_populates='favorites')
   # planet = db.relationship('Planet', back_populates='favorites')

  # def __repr__(self):
   #     return '<Favourites %r>' % self.username