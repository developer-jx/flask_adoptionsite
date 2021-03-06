# This import requires setup of db inside the __init__.py
from project import db

class Puppy(db.Model):
    __tablename__ = "puppies"

    # Table "puppies"
    # Columns:
    # - id
    # - name
    # - ownerid

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    ownerid = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.ownerid:
            return f"Puppy {self.name}, owner is {self.ownerid.name}. (ID: {self.id})"
        else:
            return f"Puppy {self.name}, no owner. (ID: {self.id})"

class Owner(db.Model):
    __tablename__ = "owners"

    # Table "owners"
    # Columns:
    # - id
    # - name
    # - puppy_id

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"{self.name}"