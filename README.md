# Puppy Adoption Site
A simple puppy adoption website based on Flask. \
Uses Flask's Jinja and Bootstrap.

Repository created in order to follow a review from a Python Flask tutorial by Pierian Data. \
*Intentionally insecure and includes the secret key.*

## Use of Virtual Environment
Highly recommend using a virtual environment in running this project. Do this before installing the dependencies, modifying modules or migrating. **Make sure that the Virtual Environment is installed in Python.** 
 1. Go inside the directory of your project (where app.py stays) 
 2. Execute this command to create a virtual env: \
	`$ python -m venv env`
 3. Enter your virtual env using this command: \
 	Bash: `$ source sys_directory/environment_name/Scripts/activate` \
	*(Example: `C:/project/env/Scripts/activate`)* \
	See the contents of folder `environment_name/Scripts` for other options. 
 4. Done! You can tell that you're inside your virtual environment when there's a `(env)` or something similar as a prefix in your terminal/bash.
 
## Dependencies
Check the requirements.txt and install all modules before starting up the project. 
 1. Install SQLite in your system through their installer. 
 2. Install the Python modules through Pip. (see requirements.txt) \
	`$ pip install -r requirements.txt`
 3. This project connects to BootstrapCDN. Make sure that the code is run on a computer with internet \
 	`https://getbootstrap.com/`
	
### Third-party issues
There's a certain issue in SQLAlchemy that still doesn't seem to be fixed. The `time.clock()` no longer exists in the latest versions of Python, so to mitigate this issue perform these changes on the modules:
 1. Head to *environment_name\Lib\site-packages\flask_sqlalchemy\__init__.py* \
	Proceed to change `time.clock` to `time.perf_counter` in Line 39.
 2. Head to *environment_name\Lib\site-packages\mako\compat.py* \
	Proceed to change `time.clock` to `time.perf_counter` in Line 124.

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

