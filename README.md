# Puppy Adoption Site
A simple puppy adoption website based on Flask. \
Uses Flask's Jinja and Bootstrap.

Repository created in order to follow a review from a Python Flask tutorial by Pierian Data. \
*Intentionally insecure and includes the secret key.*

## Dependencies
Check the requirements.txt and install all modules before starting up the project. \
 1. Install SQLite in your system through their installer. \
 2. Install the Python modules through Pip. (see requirements.tx) \
	`$ pip install -r requirements.txt`
 3. This project connects to BootstrapCDN. Make sure that the code is run on a computer with internet \
 	`https://getbootstrap.com/`

## Database
Initialize the database first through the **app.py** script in a terminal.
 1. Set Flask environment variable first, enter the directory \
 	Windows: `$ set FLASK_APP=app.py` \
	Linux/MacOS: `$ export FLASK_APP=app.py`
 2. Initialize the Database \
 	`$ flask db init`
 3. Commit the models by migrating them \
	`$ flask db migrate -m "initial commit"`
 4. Execute upgrade to apply changes \
	`$ flask db upgrade`

To update the database when adding/modifying/removing models just re-do Steps 3 and 4.

## Usage
Run the development server through Python.
 1. Make sure that you've set the environment variable already. (see Database Step 1)
 2. Run the site: \
	`$ python app.py`

