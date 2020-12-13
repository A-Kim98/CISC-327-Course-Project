import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, TicketInfo
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend homepage.
The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:
@patch('qa327.backend.get_user', return_value=test_user)
Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.
Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Moch a sample user
test_user = User(
                 email='tester@gmail.com',
                 name='tester',
                 password=generate_password_hash('Tester327!'),
                 balance=10000
            )
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Test_frontend123!'),
    balance=10000
)

test_tickets = TicketInfo(
    email='test_frontend@test.com',
    name='t1',
    quantity=1,
    price=100,
    date='20210408'
)


class IndexPageTest(BaseCase):

    #Test Case R3.1
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_user_redirect(self, *_):
        """
        This is a sample front end unit test to vertify users that are not logged in
        are redirected to the login page
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # test that redirection to /login has occurred
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R3.2
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_success(self, *_):
        """
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend123!")

        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Hi test_frontend", "#welcome-header")
        
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R3.3
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_show_balance(self, *_):
        """
        This is a sample front end unit test to vertify users that are not logged in
        are redirected to the login page
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend123!")

        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        # open home page
        self.open(base_url)
        # test if user  balance is displayed as it should
        self.assert_element("#user_balance")
        self.assert_text("Current User Balance:", "#user_balance")
        
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R3.4
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_confirm_logout(self, *_):
        """
        This is a sample front end unit test to vertify users that are not logged in
        are redirected to the login page
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend123!")

        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        # open home page
        self.open(base_url)
        # test that there's a hyperlinked text that says logout
        self.assert_link_text("logout")
        
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R3.5
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_ticket_table(self, *_):
        """
        This is a sample front end unit test to vertify users that are not logged in
        are redirected to the login page
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend123!")

        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        # open home page
        self.open(base_url)
        # test if the ticket information is displayed as it should
        self.assert_element(    "#tickets")
        self.assert_text("t1",  "#tickets")
        self.assert_text("100", "#tickets")
        self.assert_text("1",   "#tickets")
        self.assert_text("testemail@gmail.com","#tickets")
        
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R3.6
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_selling_form(self, *_):
        """
        This is a sample front end unit test to vertify users that are not logged in
        are redirected to the login page
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend123!")

        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        # open home page
        self.open(base_url)
        # test that there's a form for updateing in proper format
        self.assert_element("#sell")
        self.assert_element("#name_sell")
        self.assert_element("#quantity_sell")
        self.assert_element("#price_sell")
        self.assert_element("#expdate_sell")
        
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R3.7
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buying_form(self, *_):
        """
        This is a sample front end unit test to vertify users that are not logged in
        are redirected to the login page
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend123!")

        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        # open home page
        self.open(base_url)
        # test that there's a form for buying in proper format
        self.assert_element("#buy")
        self.assert_element("#name_buy")
        self.assert_element("#quantity_buy")
        
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R3.8
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_selling_validate(self, *_):
        """
        This is a sample front end unit test to vertify users that are not logged in
        are redirected to the login page
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend123!")

        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        # open home page
        self.open(base_url)
        # test that there's a button that allows the form to be posted to /sell
        self.assert_element("#sell")
        
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R3.9
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buying_validate(self, *_):
        """
        This is a sample front end unit test to vertify users that are not logged in
        are redirected to the login page
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend123!")

        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        # open home page
        self.open(base_url)
        # test that there's a button that allows the form to be posted to /buy
        self.assert_element("#buy")
        
        # open logout (for cleanup)
        self.open(base_url + '/logout')

    # Test Case R3.10
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_updating_validate(self, *_):
        """
        This is a sample front end unit test to vertify users that are not logged in
        are redirected to the login page
        """
        # open logout page to invalid any logged-in sessions that may exist, then open login page
        self.open(base_url + '/logout')
        self.open(base_url + '/')

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend123!")

        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        # open home page
        self.open(base_url)
        # test that there's a button that allows the form to be posted to /update
        self.assert_element("#update")
        
        # open logout (for cleanup)
        self.open(base_url + '/logout')
