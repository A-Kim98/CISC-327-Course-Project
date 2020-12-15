import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, TicketInfo
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines unit tests for the frontend homepage.
The tests will only test the frontend portion of the program, by patching the backend to return
specific values. For example:
@patch('qa327.backend.get_user', return_value=test_user)
Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.
Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

class TestRStatment(BaseCase):
    # we need users to interact if we want to cover the buy deletion so we are just going to write all the tests as
    # one big test. This test also functions as a good integration test (we could write a fixture but we have to test
    # register and login anyways
    @pytest.mark.timeout(60)
    def test_user_interact(self, *_):
        # open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open the register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "login@gmail.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "t1")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("User name has to be longer than 2 characters and less than 20 characters.", "#message")
        # proper input
        self.type("#email", "login@gmail.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "TestUser")
        self.click('input[type="submit"]')

        # register other person
        self.open(base_url + '/register')
        self.type("#email", "login2@gmail.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "TestUser2")
        self.click('input[type="submit"]')

        # test login error code that wasn't covered
        self.open(base_url + '/login')
        self.type("#email", "login@gmail.com")
        # an incorrect password
        self.type("#password", "Tesr327!")
        self.click('input[type="submit"]')
        self.assert_text("email/password combination incorrect.", "#message")
        self.type("#email", "login@gmail.com")
        # an incorrect password
        self.type("#password", "Tester327!")
        self.click('input[type="submit"]')

        # this test is currently unreachable but should be added if we decide the ticket name should be longer than 1
        '''
        # now on the home page of user1
        self.type("#name_sell", "")
        self.type("#quantity_sell", "1")
        self.type("#price_sell", "10")
        self.type("#expdate_sell", "20210901")
        # click sell button
        self.click('input[value="Sell"]')
        # assert empty error
        self.assert_text("The name of the tickets has to contain at least once character", "#sell_message")
        '''
        # now on the home page of user1
        self.type("#name_sell", "userTicket")
        self.type("#quantity_sell", "1")
        self.type("#price_sell", "10")
        self.type("#expdate_sell", "20200901")
        # click sell button
        self.click('input[value="Sell"]')
        self.assert_text("The new tickets must not be expired", "#sell_message")

        # now do a positive sell
        self.type("#name_sell", "userTicket")
        self.type("#quantity_sell", "1")
        self.type("#price_sell", "10")
        self.type("#expdate_sell", "20210901")
        # click sell button
        self.click('input[value="Sell"]')
        # logout
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "login2@gmail.com")
        self.type("#password", "Tester327!")
        self.click('input[type="submit"]')
        # now logged in as user 2 and we run code for delete ticket
        self.type("#name_buy", "userTicket")
        self.type("#quantity_buy", "1")
        # click buy button
        self.click('input[value="Buy"]')
        self.assert_text_not_visible("userTicket", "#tickets")
        # open logout (for cleanup)
        self.open(base_url + '/logout')
