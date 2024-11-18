import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)



class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):

        if password != password_confirmation:
            raise UserInputError("Password and password confirmation don't match")
        
        if not password or len(password) < 8:
            raise UserInputError("Password must be at least 8 characters")

        
        if not re.search(r'[a-zA-Z]', password) or not re.search(r'\d', password):
            raise UserInputError("Password must contain letters and numbers")

        if not username or len(username) < 3 or not re.match("^[a-z]+$", username):
            raise UserInputError("Username must be min. 3 characters and contain only lowercase letters")
        
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username is already in use")



user_service = UserService()
