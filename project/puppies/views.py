from flask import Blueprint, render_template, redirect, url_for, flash, session
from project import db
from project.models import Puppy, Owner
from project.puppies.forms import AddForm, DelForm

# Create the blueprint
puppies_blueprint = Blueprint('puppies', __name__,
                                template_folder='templates/puppies')

@puppies_blueprint.route('/puppies')
def listpuppy():
    puppieslist = Puppy.query.all()
    return render_template('listpuppy.html', puppieslist=puppieslist)

@puppies_blueprint.route('/addpuppy', methods=['GET', 'POST'])
def addpuppy():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # No ID checker since there can be multiple puppies with the same name.
        add_pup = Puppy(name)
        db.session.add(add_pup)
        db.session.commit()

        flash("Successfully added new puppy!", 'success')
        return redirect(url_for('puppies.listpuppy'))

    return render_template('addpuppy.html', form=form)

@puppies_blueprint.route('/delpuppy', methods=['GET', 'POST'])
def delpuppy():
    form = DelForm()

    if form.validate_on_submit():
        pup_id = form.pup_id.data
        owner = Owner.query.filter_by(puppy_id=pup_id).first()

        del_puppy = Puppy.query.get(pup_id)

        # Checks if the puppy exists before attempting to delete it.
        if del_puppy is not None:

            # Checks if puppy has an owner, if it does then delete the owner as well.
            if owner:
                del_owner = Owner.query.get(owner.id)

                db.session.delete(del_puppy)
                db.session.delete(del_owner)
                db.session.commit()

                flash("Successfully removed puppy.", 'success')
                return redirect(url_for('puppies.listpuppy'))
            else:
                db.session.delete(del_puppy)
                db.session.commit()

                flash("Successfully removed puppy and its assigned owner.", 'success')
                return redirect(url_for('puppies.listpuppy'))
        else:
            flash("Error: Cannot remove puppy since it doesn't exist", 'danger')
            return redirect(url_for('puppies.delpuppy'))

    return render_template('delpuppy.html', form=form)

