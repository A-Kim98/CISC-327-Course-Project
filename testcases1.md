#####Test case R1.1 - If the user hasn't logged in, show the login page
Actions:  
* open /logout (to invalidate any logged in sessions may exist)
* open /login
(validate that the current page contains the ```#login``` element

#####Test case R1.2: the login page has a message that by default says 'please login'
Actions: 
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* validate that the ```#message``` element contains the text "please login"

#####Test case R1.4 -The login page provides a login form which requests two fields: email and passwords
* open /login
* validate that the element ```input[name = "email"]``` exists
* validate that the element ```input[type = "password"]``` exists

#####Test case R1.5 - The login form can be submitted as a POST request to the current URL (/login)
* open /login
* validate that the element ```form[method = "post"]``` exists

#####Test case R1.6 - Email and password both cannot be empty
* open /login
* assert that input[required] is validated for both email and password

#####Test case R1.7 - Email has to follow addr-spec defined in RFC 5322
* open /login
* check that the email contains 

#####Test case R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
Mockup: create a test user with 

-open /login
-input a password "test!" and check error message (needs minimum length 6)
-input a password "test123! and check error message (needs at least one upper case)
-input a password "TEST123!" and check error message (needs at least one lower case)
-input a password "TESt123" and check error message (needs at least one special character)

#####Test case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
* open /login
* enter email with formatting error into element #email
* enter password with formatting error into element #password
* click element ```input[type = "submit"]```
* open /login again
* check that ```#message``` is "email/password format is incorrect"

#####Test case R1.10 - If email/password are correct, redirect to /
Mocking:
	- Mock backend.get_user to return a test_user instance
Actions:
-open /logout (to invalidate any logged in sessions may exist)
-open /login
