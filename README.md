Project description:
A full stack application built using python FASTAPI. It basically helps a user sign in and create/retrieve/complete his tasks.

Technologies used:
Postgresql -> for storing user credentials and todos-data lists.
Alembic -> for seamless data migrations
JWT and Oauth2 -> for authentication and authorization.
PyTest -> for creating test cases for various endpoints and fucntions within the app.
FASTAPI -> core backend built for api routing
Frontend was mostly built from bootstrap CSS and custom JS logic.
SQLAlchemy -> for storing database models in python.

Setup instructions:
First setup a SQL database and put the url in the SQLALCHEMY_DATABASE_URL in database.py file.
Create a virtual environment first with pip. 
pip -r requirements.txt
uvicorn TodoAPP.main:app --reload

Check swagger documentation at http://127.0.0.1:8000/docs
