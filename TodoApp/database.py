from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:sunny123@localhost/TodoAppDB'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
#This 'Base' class defines all your DB models. All model classes will inherit from Base in models.py .

#create_engine -> sets up the connection to your database. It doesn’t establish a DB connection immediately 
#but prepares for it (lazy connection).

#sessionmaker -> A factory for creating new Session objects which is further used for db interactions.
#autocommit=False: You will manually commit transactions.
#autoflush=False: Prevents automatic DB writes after every query unless explicitly done.
#bind=engine: This tells the session to use the engine we created for DB communication.

#declarative_base -> This returns a base class from which all your SQLAlchemy ORM models will inherit. It is 
#required to define tables in models.py .

#SQLALCHEMY_DATABASE_URL -> dialect+driver://username:password@hostname/dbname