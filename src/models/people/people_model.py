from .. import db


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(900), nullable=False)
    eye_color = db.Column(db.String(60), nullable=False)
    
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name
    
#metodods de instacia
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "eye_color": self.eye_color
            # do not serialize the password, its a security breach
        }