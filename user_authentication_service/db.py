#!/usr/bin/env python3

"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self,
                email: str,
                hashed_password: str
                ) -> User:
        '''Adds user to db and returns
            user object'''
        user = User()
        user.email = email
        user.hashed_password = hashed_password
        self.total_users += 1
        user.id = self.total_users
        user.session_id = str(self.total_users)
        user.reset_token = 'reset'

        session = self._session
        session.add(user)
        session.commit()

        return user
    
    def find_user_by(self, **kwargs) -> User:
        """Find and return the user matching the provided keyword args"""
        user_class = User
        session = self._session
        try:
            user = session.query(user_class).filter_by(**kwargs).one()
            return user
        except (NoResultFound, InvalidRequestError) as error:
            raise error

    def update_user(self, user_id: int, **kwargs) -> None:
        """ method that takes as argument a required user_id integer and
        arbitrary keyword arguments, and returns None."""
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)
        session = self._session
        session.commit()
        return None
