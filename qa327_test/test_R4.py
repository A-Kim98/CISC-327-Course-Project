import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines unit tests for the frontend homepage.
The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:
@patch('qa327.backend.get_user', return_value=test_user)
Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.
Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Mock a smple user (login)
test_user_login = User(
    email='login@gmail.com',
    name='LetsTestL',
    password=generate_password_hash('Tester327!'),
    balance=10000
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100', 'email': 'testemail@gmail.com', 'quantity': '1'}
]


class TestR4(BaseCase):

    # Test Case R4.0.1
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    def test_positive_sell(self, *_):
        """
        Checking for positive case for the fields of ticket's selling form with lower boundaries
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # test that redirection to /login has occurred
        # fill email and password
        self.type("#email", test_user_login.email)
        self.type("#password", "Tester327!")

        # click enter button
        self.click('input[type="submit"]')

        # enter Sell ticket form with low values
        self.type("#name_sell", "Hello World 123")
        self.type("#quantity_sell", 1)
        self.type("#price_sell", 10)
        self.type("#expdate_sell", 20210901)
        # click sell button
        self.click('input[value="Sell"]')
        # assert no error text appears
        self.assert_text_not_visible("Ticket name must be alphanumeric-only", "#message")
        self.assert_text_not_visible("Ticket name cannot begin with a space", "#message")
        self.assert_text_not_visible("Ticket name cannot end with a space", "#message")
        self.assert_text_not_visible("Ticket name cannot be longer than 60 characters", "#message")
        self.assert_text_not_visible("At least 1 ticket must be sold", "#message")
        self.assert_text_not_visible("At most 100 tickets can be sold", "#message")
        self.assert_text_not_visible("Price of the ticket cannot be below 10", "#message")
        self.assert_text_not_visible("Price of the ticket cannot be above 100", "#message")
        self.assert_text_not_visible("Expiration date is in invalid format", "#message")
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R4.0.2
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    def test_positive_sell_high(self, *_):
        """
        Checking for positive case for the fields of ticket's selling form with higher boundaries
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # test that redirection to /login has occurred
        # fill email and password
        self.type("#email", test_user_login.email)
        self.type("#password", "Tester327!")

        # click enter button
        self.click('input[type="submit"]')
        # enter Sell ticket form with low values
        self.type("#name_sell", "Hello World 123")
        self.type("#quantity_sell", 100)
        self.type("#price_sell", 100)
        self.type("#expdate_sell", 20210901)
        # click sell button
        self.click('input[value="Sell"]')
        #asser no error text appears
        self.assert_text_not_visible("Ticket name must be alphanumeric-only", "#message")
        self.assert_text_not_visible("Ticket name cannot begin with a space", "#message")
        self.assert_text_not_visible("Ticket name cannot end with a space", "#message")
        self.assert_text_not_visible("Ticket name cannot be longer than 60 characters", "#message")
        self.assert_text_not_visible("At least 1 ticket must be sold", "#message")
        self.assert_text_not_visible("At most 100 tickets can be sold", "#message")
        self.assert_text_not_visible("Price of the ticket cannot be below 10", "#message")
        self.assert_text_not_visible("Price of the ticket cannot be above 100", "#message")
        self.assert_text_not_visible("Expiration date is in invalid format", "#message")
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R4.1.1
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    def test_alphanumeric_only(self, *_):
        """
        Check if name of the ticket is alphanumeric-only
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # test that redirection to /login has occurred
        # fill email and password
        self.type("#email", test_user_login.email)
        self.type("#password", "Tester327!")

        # click enter button
        self.click('input[type="submit"]')
        # enter Sell ticket form with low values
        self.type("#name_sell", "Ht1&t2@!*\")(/.,<>[]-+")
        self.type("#quantity_sell", 1)
        self.type("#price_sell", 15)
        self.type("#expdate_sell", 20210901)
        # click sell button
        self.click('input[value="Sell"]')
        # assert proper error message
        self.assert_text("The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the "
                         "first or the last character.", "#message") 

        # open logout (for cleanup)
        self.open(base_url + '/logout')
