### DJANGO API PROJECT

#### Description

This is a Python App api that accepts a rest request to allow admin users to view and edit the users and groups in the system.

The response to the rest request returns whether the api call  was successful and a list of users available.

#### Lanuage Used

> Python

#### Technology Requirements

> Django and 
> djangorestframework


#### How to run the project

`git clone https://github.com/baronntambwe/Python.git`

`cd api_tutorial`

`python3 -m venv env`

`source env/bin/activate` or on Windows use `env\Scripts\activate`

`pip install django` 
`pip install djangorestframework`
`python manage.py runserver`



#### How to run the tests

`curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/`


