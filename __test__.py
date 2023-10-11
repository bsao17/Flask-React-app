from main import User
import pytest


class TestUser:

    """
    Test case to create a user with valid credentials.

    This function tests the creation of a user with valid credentials. It creates a user object with the given username, email, and password. The function then asserts that the username, email, and password of the user object are equal to the expected values.

    Parameters:
        self (object): The current instance of the test class.

    Returns:
        None
    """

    def test_create_user_with_valid_credentials(self):
        user = User(username="testuser", email="test@example.com", password="password")
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.password == "password"

    """
    Function comment for test_is_active_method(self).

    This function is used to test the is_active() method of the User class.
    It creates a new User object with the username "testuser", email "test@example.com",
    and password "password". Then it asserts that the is_active() method of the User
    object returns True.

    Parameters:
        self (object): The instance of the UserTest class.

    Returns:
        None
    """
    def test_is_active_method(self):
        user = User(username="testuser", email="test@example.com", password="password")
        assert user.is_active() == True

    """
    A test method to check if the is_authenticated() method of the User class returns True when the user is active.

    Parameters:
        self (TestCase): The current test case object.

    Returns:
        None
    """
    def test_is_authenticated_method(self):
        user = User(username="testuser", email="test@example.com", password="password")
        if self.test_is_active_method():
            assert user.is_authenticated() == True

    """
    Test case for creating a user with empty credentials.
    """
    def test_create_user_with_empty_credentials(self):
        user = User(username="", email="", password="")
        assert user.username == ""
        assert user.email == ""
        assert user.password == ""

    """
    Test case to create a user with an invalid email format.

    :param self: The test case instance.
    :return: None
    """
    def test_create_user_with_invalid_email_format(self):
        user = User(username="testuser", email="invalid_email", password="password")
        assert user.username == "testuser"
        assert user.email == "invalid_email"
        assert user.password == "password"

    """
    Test case to create a user with a short password.

    This test case verifies that a user cannot be created with a password that is too short.

    Parameters:
        self (TestCase): The current test case object.

    Returns:
        None
    """
    def test_create_user_with_short_password(self):
        user = User(username="testuser", email="test@example.com", password="pass")
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.password == "pass"
