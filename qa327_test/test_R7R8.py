import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
)

# Mock some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]


class TestR7R8(BaseCase):

    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_logout_invalidates_session_redirects(self, *_):
        # open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # open home page
        self.open(base_url)
        # open logout again
        self.open(base_url + '/logout')

        self.assert_element("#login-header")
        self.assert_text("Log In", "#login-header")

    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_logout_noAccess_restricted(self, *_):
        # open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # attempt to open user page
        self.open(base_url + '/')
        # assert we are still on login page
        self.assert_element("#login-header")
        self.assert_text("Log In", "#login-header")

    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_404_error(self, *_):
        # open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/thisPageDoesNotExist')
        # assert we get a 404 error page
        self.assert_element("#404-pError")
        self.assert_text("The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.", "#404-pError")