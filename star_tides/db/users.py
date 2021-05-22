'''star_tides.db.users

This file contains classes and utilities for working with User objects in the
KB database.
'''

from typing import List, NamedTuple, Text
from enum import Enum


class UserPrivelege(Enum):
    UNKNOWN = 0
    ADMIN = 1
    COLLABORATOR = 2

class User(NamedTuple):
    id: Text
    contact_id: Text
    username: Text
    login_email: Text
    password_hash: Text
    privilege: UserPrivelege

    def to_dict(self):
        return {
            'id': self.id,
            'contact_id': self.contact_id,
            'username': self.username,
            'login_email': self.login_email,
            'password_hash': self.password_hash,
            'privelege': str(self.privilege),
        }


class UsersCollection():
    '''
    UsersCollection abstracts CRUD (etc.) operations on the Mongo Users
    collection.
    '''

    def get_user(self, unused_id: Text) -> User:
        raise NotImplementedError()

    def list_users(self) -> List[User]:
        raise NotImplementedError()

    def create_user(self, user: User) -> User:
        raise NotImplementedError()

    def delete_user(self, unused_id: Text) -> None:
        raise NotImplementedError()
