from main import User
import pytest


class TestUser:

    #  Create a User object with valid username, email and password.
    def test_create_user_with_valid_credentials(self):
        user = User(username="testuser", email="test@example.com", password="password")
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.password == "password"

    #  Call is_active() method on a User object.
    def test_is_active_method(self):
        user = User(username="testuser", email="test@example.com", password="password")
        assert user.is_active() == True

    #  Call is_authenticated() method on a User object.
    def test_is_authenticated_method(self):
        user = User(username="testuser", email="test@example.com", password="password")
        if self.test_is_active_method():
            assert user.is_authenticated() == True

    #  Create a User object with empty username, email and password.
    def test_create_user_with_empty_credentials(self):
        user = User(username="", email="", password="")
        assert user.username == ""
        assert user.email == ""
        assert user.password == ""

    #  Create a User object with invalid email format.
    def test_create_user_with_invalid_email_format(self):
        user = User(username="testuser", email="invalid_email", password="password")
        assert user.username == "testuser"
        assert user.email == "invalid_email"
        assert user.password == "password"

    #  Create a User object with password length less than 8 characters.
    def test_create_user_with_short_password(self):
        user = User(username="testuser", email="test@example.com", password="pass")
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.password == "pass"
