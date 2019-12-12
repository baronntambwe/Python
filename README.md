## To run the DJango API project


### Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

### Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

### We're now ready to test the API we've built. Let's fire up the server from the command line.

python manage.py runserver

### We can now access our API, both from the command-line, using tools like curl...

curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/
