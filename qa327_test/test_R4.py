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
    @patch('qa327.backend.get_user', return_value= test_user_login)
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


        self.type("#name_sell", "Hello World 123")
        self.type("#quantity_sell", 1)
        self.type("#price_sell", 10)
        self.type("#expdate_sell", 20210901)

        self.click('input[value="Sell"]')

        self.assert_text_not_visible("Ticket name must be alphanumeric-only", "#message")
        # open logout (for cleanup)
        self.open(base_url + '/logout')