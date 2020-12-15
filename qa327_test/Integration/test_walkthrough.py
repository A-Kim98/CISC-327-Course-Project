import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, TicketInfo
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

# Mock a sample user (login)
test_user_login = User(
    email='login@gmail.com',
    name='LetsTestL',
    password=generate_password_hash('Tester327!'),
    balance=10000
)

# Moch some sample tickets
test_tickets = TicketInfo(
    email='differentUser@gmail.com',
    name='t1',
    quantity=10,
    price=10,
    date='20210408'
)
allTickets = [test_tickets]


class TestRI(BaseCase):
    # integration test
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    def test_positive_sell_walkthrough(self, *_):
        """
        navigate through a sell and confirm a sell alters proper stuff
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
        self.type("#name_sell", "HelloWorld123")
        self.type("#quantity_sell", "10")
        self.type("#price_sell", "10")
        self.type("#expdate_sell", "20210901")
        # click sell button
        self.click('input[value="Sell"]')
        # asser no error text appears
        self.assert_text_not_visible("Ticket name must be alphanumeric-only", "#message")
        self.assert_text_not_visible("Ticket name cannot begin with a space", "#message")
        self.assert_text_not_visible("Ticket name cannot end with a space", "#message")
        self.assert_text_not_visible("Ticket name cannot be longer than 60 characters", "#message")
        self.assert_text_not_visible("At least 1 ticket must be sold", "#message")
        self.assert_text_not_visible("At most 100 tickets can be sold", "#message")
        self.assert_text_not_visible("Price of the ticket cannot be below 10", "#message")
        self.assert_text_not_visible("Price of the ticket cannot be above 100", "#message")
        self.assert_text_not_visible("Expiration date is in invalid format", "#message")
        # assert a table update
        self.assert_text("HelloWorld123", "#tickets")
        self.assert_text("1", "#tickets")
        self.assert_text("10", "#tickets")
        self.assert_text("20210901", "#tickets")
        self.assert_text("login@gmail.com", "#tickets")
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # integration test buy
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    @patch('qa327.backend.get_all_tickets', return_value=allTickets)
    def test_positive_buy_walkthrough(self, *_):
        """
           navigate through a buy and confirm buy alters information
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

        # enter buy ticket form with low values
        self.type("#name_buy", "t1")
        self.type("#quantity_buy", "3")

        # click buy button
        self.click('input[value="Buy"]')
        # assert no error text appears
        self.assert_text_not_visible("Ticket name must be alphanumeric-only", "#message")  # TODO update these asserts
        self.assert_text_not_visible("Ticket name cannot begin with a space", "#message")
        self.assert_text_not_visible("Ticket name cannot end with a space", "#message")
        self.assert_text_not_visible("Ticket name cannot be longer than 60 characters", "#message")
        self.assert_text_not_visible("At least 1 ticket must be sold", "#message")
        self.assert_text_not_visible("At most 100 tickets can be sold", "#message")
        self.assert_text_not_visible("Price of the ticket cannot be below 10", "#message")
        self.assert_text_not_visible("Price of the ticket cannot be above 100", "#message")
        self.assert_text_not_visible("Expiration date is in invalid format", "#message")

        # assert table update
        self.assert_text("t1", "#tickets")
        self.assert_text("7", "#tickets")
        self.assert_text("10", "#tickets")
        self.assert_text("20210408", "#tickets")
        self.assert_text("differentUser@gmail.com", "#tickets")

        self.open(base_url + '/logout')
