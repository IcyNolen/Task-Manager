from .database import Base
#Since, this models.py and database.py are in the same directory(TodoApp/), you must be thinking why to apply the
#dot before database word, but it is important as relative imports are safer instead of absolute imports,
#or else python will have to search whole directories for it which may give errors for same name files.
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

#Defines a model class Users which maps to the 'users' table in DB.
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    phone_number = Column(String)


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
