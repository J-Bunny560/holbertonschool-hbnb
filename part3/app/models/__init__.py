from sqlalchemy.ext.declarative import declarative_base
from .user import User
from .amenity import Amenity
from .place import Place
from .review import Review

Base = declarative_base()
