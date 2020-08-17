import os
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from forms import AddPuppyForm, DelPuppyForm, AddOwnerForm, DelOwnerForm

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = "somekey13131"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Models
class Puppy(db.Model):
    __tablename__ = "puppies"

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

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"{self.name}"

# Views
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/puppies')
def listpuppy():
    puppieslist = Puppy.query.all()
    return render_template('listpuppy.html', puppieslist=puppieslist)

@app.route('/addpuppy', methods=['GET', 'POST'])
def addpuppy():
    form = AddPuppyForm()

    if form.validate_on_submit():
        name = form.name.data

        add_pup = Puppy(name)
        db.session.add(add_pup)
        db.session.commit()
        flash("Successfully added new puppy!", 'success')
        return redirect(url_for('listpuppy'))

    return render_template('addpuppy.html', form=form)

@app.route('/delpuppy', methods=['GET', 'POST'])
def delpuppy():
    form = DelPuppyForm()

    if form.validate_on_submit():
        pup_id = form.pup_id.data
        owner = Owner.query.filter_by(puppy_id=pup_id).first()

        del_puppy = Puppy.query.get(pup_id)
        db.session.delete(del_puppy)

        if owner:
            del_owner = Owner.query.get(owner.id)
            db.session.delete(del_owner)

        db.session.commit()

        flash("Successfully removed puppy.", 'success')
        return redirect(url_for('listpuppy'))

    return render_template('delpuppy.html', form=form)

@app.route('/owners')
def listowner():
    ownerslist = Owner.query.all()
    return render_template('listowner.html', ownerslist=ownerslist)

@app.route('/addowner', methods=['GET', 'POST'])
def addowner():
    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data

        add_owner = Owner(name, pup_id)
        db.session.add(add_owner)
        db.session.commit()
        
        flash("Successfully added new owner.", 'success')
        return redirect(url_for('listowner'))

    return render_template('addowner.html', form=form)

@app.route('/delowner', methods=['GET', 'POST'])
def delowner():
    form = DelOwnerForm()

    if form.validate_on_submit():
        owner_id = form.owner_id.data

        del_owner = Owner.query.get(owner_id)
        db.session.delete(del_owner)
        db.session.commit()

        flash("Successfully removed owner.", 'success')
        return redirect(url_for('listowner'))

    return render_template('delowner.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)