#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage():
    """connect to MySQL database"""
    __engine = None
    __session = None
    #  __user = os.getenv("HBNB_MYSQL_USER")
    #  __passwd = os.getenv("HBNB_MYSQL_PWD")
    #  __host = os.getenv("HBNB_MYSQL_HOST")
    #  __db = os.getenv("HBNB_MYSQL_DB")
    #  __dialect = "mysql"
    #  __driver = "mysqldb"
    #  __SQL_str = "{}+{}://{}:{}@{}/{}"

    def __init__(self):
        self.__engine = create_engine("{}+{}://{}:{}@{}/{}".
                                      format("mysql", "mysqldb",
                                             os.getenv("HBNB_MYSQL_USER"),
                                             os.getenv("HBNB_MYSQL_PWD"),
                                             os.getenv("HBNB_MYSQL_HOST"),
                                             os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls-None):
        """ Query on current database for all o specify class"""
        dic = {}
        types_obj = [State, City, User, Ammenity, Place, Review]

        if cls is not None and cls in types_obj:
            query_list = self.__session.query(cls).all()
            for el in query_list:
                dic[el.to_dict()['__class__'] + '.' + el.id] = el
        else:
            for typ in types_obj:
                query_list2 = self.__session.query(typ).all()
                for el2 in query_list2:
                    dic[el2.to_dict()['__class__'] + '.' + el2.id] = el2
        return dic

    def new(self, obj):
        """add the object to the current DB session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current DB session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current DB session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """call remove method on the private session attribute"""
        self.__session.remove()
