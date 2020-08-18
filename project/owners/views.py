from flask import Blueprint, render_template, redirect, url_for, flash, session
from project import db
from project.models import Owner, Puppy
from project.owners.forms import AddForm, DelForm

# Create the blueprint
owners_blueprint = Blueprint('owners', __name__,
                                template_folder='templates/owners')

@owners_blueprint.route('/owners')
def listowner():
    ownerslist = Owner.query.all()
    return render_template('listowner.html', ownerslist=ownerslist)

@owners_blueprint.route('/add', methods=['GET', 'POST'])
def addowner():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data

        puppy_to_assign = Puppy.query.get(pup_id)

        # This if-statement checks if the Puppy exists.
        if puppy_to_assign is not None:

            # This checks if puppy already has an owner.
            if puppy_to_assign.ownerid is None:
                add_owner = Owner(name, pup_id)
                db.session.add(add_owner)
                db.session.commit()

                flash("Successfully added new owner.", 'success')
                return redirect(url_for('owners.listowner'))
            else:
                flash("Error: Cannot add owner. Puppy already has one.", 'danger')
                return redirect(url_for('owners.addowner'))
        else:
            flash("Error: Cannot add new owner. Puppy ID provided does not exist.", 'danger')
            return redirect(url_for('owners.addowner'))

    return render_template('addowner.html', form=form)

@owners_blueprint.route('/del', methods=['GET', 'POST'])
def delowner():
    form = DelForm()

    if form.validate_on_submit():
        owner_id = form.owner_id.data
        del_owner = Owner.query.get(owner_id)

        # This checks if the owner exists before deleting it.
        if del_owner is not None:
            db.session.delete(del_owner)
            db.session.commit()
            flash("Successfully removed owner.", 'success')
            return redirect(url_for('owners.listowner'))
        else: 
            flash("Error: Cannot delete owner since it does not exist.", 'danger')
            return redirect(url_for('owners.delowner'))

    return render_template('delowner.html', form=form)