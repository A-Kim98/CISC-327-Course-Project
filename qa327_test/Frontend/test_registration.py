import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


'''
    This file defines all unit tests for the frontend homepage (R1 and R2).
'''

# Mock a sample user (register)
test_user_register = User(
                 email='registration@gmail.com',
                 password=generate_password_hash('Tester327!'),
                 name='LetsTestR',
                 balance=5000,
                 tickets = None
            )
  
# Mock a smple user (login)
test_user_login = User(
                 email='login@gmail.com',
                 name='LetsTestL',
                 password=generate_password_hash('Tester327!'),
                 balance=10000
            )

# Mock some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100', 'email' : 'testemail@gmail.com', 'quantity': '1'}
]


class FrontEndHomePageTest(BaseCase):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                        R2 - Register
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    # R2.2- Show the user registration page if user is not logged in
    def test_register(self, *_):
        # open the logout page to invalidate any logged-in session
        self.open(base_url + '/logout')
        #open the register page
        self.open(base_url + '/register')
        #make sure it shows the proper page and message
        self.assert_element("#welcome-header")
        self.assert_text("Hi there!", "#welcome-header")
        
    
    # R2.3 - The registration page shows a registration form requesting: email, user name, password, password2
    @pytest.mark.timeout(60)
    def test_register_form(self, *_):
        #open the register page
        self.open(base_url + '/register')
        self.type("#email", "")
        self.type("#name", "")
        self.type("#password", "")
        self.type("#password2", "")
        self.click('input[type="submit"]')

    
    # R2.4 - The registration form can be submitted as a POST request to the current URL (/register)
    # R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
    @pytest.mark.timeout(60)
    def test_register_success(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill the form
        self.type("#email", "test_registration@gmail.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        #open the login page
        self.open(base_url + '/login')
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Hi there!", "#welcome-header")
        #open logout page
        self.open(base_url + '/logout')
    
    
    #R2.5 - Email, password, password2 all have to satisfy the same required as defined in R1
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_empty_email_case1(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        #open the register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", " ")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email and/or password cannot be empty.", "#message")
        #open logout page
        self.open(base_url + '/logout')
    

    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_empty_password_case1(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        #open the register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "tester123@gmail.com")
        self.type("#password", " ")
        self.type("#password2", " ")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email and/or password cannot be empty.", "#message")
        #open logout page
        self.open(base_url + '/logout')
    
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_emtpy_email_password_case2(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        #open the register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", " ")
        self.type("#password", " ")
        self.type("#password2", " ")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email and/or password cannot be empty.", "#message")
        #open logout page
        self.open(base_url + '/logout')
    
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_email_format_case1(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        #open the register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "1234567890123456789012345678901234567890123456789012345678901234+x@example.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
        #open logout page
        self.open(base_url + '/logout')
    
    # Email has to follow addr-spec defined in RFC 5322
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_email_format_case2(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        #open the register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "abc@superlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octets.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
        #open logout page
        self.open(base_url + '/logout')
        
    # Email has to follow addr-spec defined in RFC 5322
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_email_format_case3(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        #open the register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "abc.example.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
        #open logout page
        self.open(base_url + '/logout')
    
    # Email has to follow addr-spec defined in RFC 5322
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_email_format_case4(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        #open the register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "a'b(c)d,e:f;g<h>i[j\\k]l@example.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
        #open logout page
        self.open(base_url + '/logout')
        
    # Email has to follow addr-spec defined in RFC 5322
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_email_format_case5(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        #open the register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "i_like_underscore@but_its_not_allow_in_this_part.example.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
        #open logout page
        self.open(base_url + '/logout')

    # Password has to meet the required complexity: minimum length 6
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_password_failed_case1(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill wrong email and password
        self.type("#email", "test_registration@test.com")
        self.type("#password", "test!")
        self.type("#password2", "test!")
        self.type("#name", "test_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")
        #open logout page
        self.open(base_url + '/logout')
   
    # Password needs at least one upper case.
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_password_failed_case2(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill wrong email and password
        self.type("#email", "test_registration@test.com")
        self.type("#password", "test123!")
        self.type("#password2", "test123!")
        self.type("#name", "test_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")
        #open logout page
        self.open(base_url + '/logout')
    
    # Password needs at least one lower case.
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_password_failed_case3(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill wrong email and password
        self.type("#email", "test_registration@test.com")
        self.type("#password", "TEST123!")
        self.type("#password2", "TEST123!")
        self.type("#name", "test_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")
        #open logout page
        self.open(base_url + '/logout')
    
    # Password needs at least one special character.
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_password_failed_case4(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill wrong email and password
        self.type("#email", "test_registration@test.com")
        self.type("#password", "TESt123")
        self.type("#password2", "TESt123")
        self.type("#name", "test_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")
        #open logout page
        self.open(base_url + '/logout')
      
    # R2.6 - Password and password2 have to be exactly the same
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_password_failed_case5(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill wrong email and password
        self.type("#email", "test_registration@test.com")
        self.type("#password", "Test_frontend")
        self.type("#password2", "Test_frontend!")
        self.type("#name", "test_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")
        #open logout page
        self.open(base_url + '/logout')


    #R2.7 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_username_failed_case1(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill wrong email and password
        self.type("#email", "test_registration@test.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", " ")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("User name has to be non-empty.", "#message")
        #open logout page
        self.open(base_url + '/logout')

    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_username_failed_case2(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill wrong email and password
        self.type("#email", "test_registration@test.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "1234")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("User name has to be alphanumeric-only", "#message")
        #open logout page
        self.open(base_url + '/logout')
            
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_username_failed_case3(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill wrong email and password
        self.type("#email", "test_registration@test.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", " testuser")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Space allowed only if it is not the first or the last character.", "#message")
        #open logout page
        self.open(base_url + '/logout')
            
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_username_failed_case4(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill wrong email and password
        self.type("#email", "test_registration@test.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "testuser ")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Space allowed only if it is not the first or the last character", "#message")
        #open logout page
        self.open(base_url + '/logout')


    #R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)
    #password error
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_format_error_case1(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill the form
        self.type("#email", "test_registration@test.com")
        self.type("#password", "!@)#$(@#$(!@#)$)@#($)!)@(#$#(")
        self.type("#password2", "Tester327!")
        self.type("#name", "tester")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")
        #open logout page
        self.open(base_url + '/logout')
    
    #password2 error
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_format_error_case2(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill the form
        self.type("#email", "test_registration@test.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "!@)#$(@#$(!@#)$)@#($)!)@(#$#(")
        self.type("#name", "tester" )
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Passwords do not match", "#message")
        #open logout page
        self.open(base_url + '/logout')
 
    #name error
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_register_format_error_case3(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill the form
        self.type("#email", "test_registration@test.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "!@)#)#(")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Incorrect Name format!", "#message")
        #open logout page
        self.open(base_url + '/logout')
            

    # R2.10 - If the email already exists, show message 'this email has been ALREADY used'
    @pytest.mark.timeout(60)
    @patch('qa327.backend.register_user', return_value=test_user_register)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.get_user', return_value=test_user_register)
    def test_register_check_email(self, *_):
        #open the register page
        self.open(base_url + '/register')
        # fill the form
        self.type("#email", "test_registration@gmail.com")
        self.type("#password", "Tester327!")
        self.type("#password2", "Tester327!")
        self.type("#name", "LetsTestR")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("This email has been ALREADY used.", "#message")
        #open logout page
        self.open(base_url + '/logout')
    

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                        R1 - Login
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    

    # R1.1 - If the user hasn't logged in, show the login page
    @pytest.mark.timeout(60)
    def test_login(self, *_):
        # open the logout page to invalidate any logged-in session
        self.open(base_url + '/logout')
        #open the login page
        self.open(base_url + '/login')
        #make sure it shows the proper page
        self.assert_element("#welcome-header")
    
    
    # R1.2: the login page has a message that by default says 'please login'
    @pytest.mark.timeout(60)
    def test_login_message(self, *_):
        # Open the logout page to invalidate any logged-in session
        self.open(base_url + '/logout')
        # open the login page
        self.open(base_url + '/login')
        # make sure it shows the proper page and message
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
    
    
    # R1.3: If the user has logged in, redirect to the user profile page
    # R1.5 - The login form can be submitted as a POST request to the current URL (/login)
    # R1.10 - If email/password are correct, redirect to /
    # R2.1 If the user has logged in, redirect back to the user profile page /
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_success(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "tester@gmail.com")
        self.type("#password", "Tester327!")
        # click enter button
        self.click('input[type="submit"]')
        # open home page
        self.open(base_url)

    # R1.4 -The login page provides a login form which requests two fields: email and passwords
    @pytest.mark.timeout(60)
    def test_login_form(self, *_):
        self.open(base_url + '/login')
        self.type("#email", "")
        self.type("#password", "")
        self.click('input[type="submit"]')

    # R1.6.1 - Email and password both cannot be empty [Email]
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_empty_email(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", " ")
        self.type("#password", "Test123!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email and/or password cannot be empty.", "#message")
    
    # R1.6.2 - Email and password both cannot be empty [Password]
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_empty_password(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "tester@gmail.com")
        self.type("#password", " ")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email and/or password cannot be empty.", "#message")
        
    # R1.6.3 - Email and password both cannot be empty [Email and Password]
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_emtpy_email_password(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", " ")
        self.type("#password", " ")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email and/or password cannot be empty.", "#message")

    # R1.7.1 - Email has to follow addr-spec defined in RFC 5322
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @pytest.mark.timeout(60)
    def test_login_email_format_case1(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "1234567890123456789012345678901234567890123456789012345678901234+x@example.com")
        self.type("#password", "Test123!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
    
    # R1.7.2 - Email has to follow addr-spec defined in RFC 5322
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @pytest.mark.timeout(60)
    def test_login_email_format_case2(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "abc@superlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octetssuperlongdomainnamethatisover255octets.com")
        self.type("#password", "Test123!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
        
    # R1.7.3 - Email has to follow addr-spec defined in RFC 5322
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @pytest.mark.timeout(60)
    def test_login_email_format_case3(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "abc.example.com")
        self.type("#password", "Test123!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
    
    # R1.7.4 - Email has to follow addr-spec defined in RFC 5322
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @pytest.mark.timeout(60)
    def test_login_email_format_case4(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "a'b(c)d,e:f;g<h>\\i[j]l@example.com")
        self.type("#password", "Test123!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
    
    # R1.7.5 - Email has to follow addr-spec defined in RFC 5322
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @pytest.mark.timeout(60)
    def test_login_email_format_case5(self, *_):
        #open logout page to invalidate any logged in sessions may exist
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "i_like_underscore@but_its_not_allow_in_this_part.example.com")
        self.type("#password", "Test123!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect.", "#message")
   
    # minimum length 6
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_password_failed_case1(self, *_):
        # open login page
        self.open(base_url + '/login')
        # fill wrong email and password
        self.type("#email", "tester@test.com")
        self.type("#password", "test!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")

    # minimum length 6
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_password_failed_case2(self, *_):
        # open login page
        self.open(base_url + '/login')
        # fill wrong email and password
        self.type("#email", "tester@test.com")
        self.type("#password", "test123!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")

    # at least one lower case
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_password_failed_case3(self, *_):
        # open login page
        self.open(base_url + '/login')
        # fill wrong email and password
        self.type("#email", "tester@test.com")
        self.type("#password", "TEST123!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")
        
    
    # at least one special character.
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_password_failed_case4(self, *_):
        # open login page
        self.open(base_url + '/login')
        # fill wrong email and password
        self.type("#email", "tester@test.com")
        self.type("#password", "TESt123")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")
    
    # R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_format_error(self, *_):
        # open login page
        self.open(base_url + '/login')
        # fill wrong email and password
        self.type("#email", "!@)#$(@#$(!@#)$)@#($)!)@(#$#(")
        self.type("#password", "Test123!")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect", "#message")
        
    # R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
    @pytest.mark.timeout(60)
    @patch('qa327.backend.get_user', return_value=test_user_login)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_format_error(self, *_):
        # open login page
        self.open(base_url + '/login')
        # fill wrong email and password
        self.type("#email", "tester@gmail.com")
        self.type("#password", "!@)#$(@#$(!@#)$)@#($)!)@(#$#(")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.", "#message")
