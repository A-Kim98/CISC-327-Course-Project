# CISC-327-Course-Project

Test data:  
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
    balance = 0
)
```
#### Test case R2.5 - Email, password, password2 all have to satisfy the same required as defined in R1

#### R2.5.1
Actions:
* Open /logout (to invalid any logged-in sessions may exist)
* open /register
* enter ```1234567890123456789012345678901234567890123456789012345678901234+x@example.com``` into element ```#email```
* input a test_user's password in element ```#password```
* click element ```input[type = "submit"]```
* check that ```#message``` is "Email/password format is incorrect."
* Open /logout (clean up)

#### R2.5.2.1
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter the value "" into element ```#password```
* click element ```input[type="submit"]```
* validate that user receive error ```#message``` "Password cannot be empty"
* Open /logout (clean up)

#### R2.5.2.2
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter the value "" into element ```#password2```
* click element ```input[type="submit"]```
* validate that user receive error ```#message``` "Password cannot be empty"
* Open /logout (clean up)

#### R2.5.2.3
Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's password into element ```#password```
* enter the "" into element ```#email``` and click ```input[type="submit"]```
* validate that you receive error ```#message``` "Email cannot be empty"
* Open /logout (clean up)

#### R2.5.2.4
Actions: 
* open /login
* enter the "" into element ```#email``` and  ```#password```
* click ```input[type="submit"]```
* validate that you receive error ```#message``` "Email and/or password cannot be empty"
* Open /logout (clean up)

#### R2.5.3.1
Actions: 
* open /login
* input test_user's email into ```#email```
* input a password "test!"  into ```#password```
* click element ```input[type = "submit"]```
* check  element ```#message``` is "Password needs minimum length 6" 
* Open /logout (clean up)

#### R2.5.3.2
Actions:
* open /login
* input test_user's email into ```#email```
* input a password "test123!  into ```#password```
* click element ```input[type = "submit"]```
* check element ```#message``` is "Password needs at least one upper case"
* Open /logout (clean up)

#### R2.5.3.3
Actions:
* open /login
* input test_user's email into ```#email```
* input a password "TEST123!"  into ```#password```
* click element ```input[type = "submit"]```
* check element ```#message``` is "Password needs at least one lower case."
* Open /logout (clean up)

#### R2.5.3.4
Actions:
* open /login.
* input test_user's email into ```#email```
* input a password "tESt123"  into ```#password```
* click element ```input[type = "submit"]```
* check element ```#message``` is "Password needs at least one special character." 
* check that ```#password``` meets the required complexity
* check that ```#password2``` meets the required complexity
* Open /logout (clean up)

#### Test case R2.6 - Password and password2 have to be exactly the same
Actions:
* open /register
* check that content of ```#password``` and ```#password2``` are equal

#### Test case R2.7 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.

#### R2.7.1
Actions:
* open /register
* input a user name "" into ```#name```
* check that  ```#message``` is "User name has to be non-empty."


#### R2.7.2
Actions:
* open /register
* input a user name "1234" into ```#name```
* check that ```#message``` is "User name has to be alphanumeric-only"

#### R2.7.3
Actions:
* open /register
* input a user name " testuser" into ```#name```
* check that ```#message``` is "Space allowed only if it is not the first or the last character."

#### R2.7.4
Actions:
* open /register
* input a user name "testuser " into ```#name```
* check that  ```#message``` is "Space allowed only if it is not the first or the last character."

#### Test case R2.8 - User name has to be longer than 2 characters and less than 20 characters.
#### R2.8.1
Actions:
* open /register
* input a user name "a" into ```#name```
* check that  ```#message``` is "User name has to be longer than 2 characters."

#### R2.8.2
Actions:
* open /register
* input a user name "Polytetrafluoroethylene" into ```#name```
* check that  ```#message``` is "User name has to be less than 20 characters."

#### Test case R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)

#### R2.9.1
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /register
* enter email with formatting error into element ```#email```
* enter password with test_user's password into element ```#password```
* enter name with test_user' name into element ```#name```
* enter password2 with test_user's password into element ```#password2```
* click element ```input[type = "submit"]```
* open /login
* check that ```#message``` is "{} format is incorrect."
* Open /logout (clean up)

#### R2.9.2
* Mock backend.get_user to return a test_user instance

Actions:
* open /register
* enter email with test_user's email into element ```#email```
* enter password with formatting error into element ```#password```
* enter name with test_user' name into element ```#name```
* enter password2 with test_user's password into element ```#password2```
* click element ```input[type = "submit"]```
* open /login
* check that ```#message``` is "{} format is incorrect."
* Open /logout (clean up)

#### R2.9.3
* Mock backend.get_user to return a test_user instance

Actions:
* open /register
* enter email with test_user's email into element ```#email```
* enter password with test_user's password into element ```#password```
* enter name with formatting error into element ```#name```
* enter password2 with test_user's password into element ```#password2```
* click element ```input[type = "submit"]```
* open /login
* check that ```#message``` is "{} format is incorrect."
* Open /logout (clean up)

#### R2.9.4
* Mock backend.get_user to return a test_user instance

Actions:
* open /register
* enter email with test_user's email into element ```#email```
* enter password with test_user's password into element ```#password```
* enter name with test_user' name into element ```#name```
* enter password2 with formatting error into element ```#password2```
* click element ```input[type = "submit"]```
* open /login
* check that ```#message``` is "{} format is incorrect."
* Open /logout (clean up)

#### Test case R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)

#### R2.9.1
Mocking:
* Mock backend.get_user to return a test_user instance
Actions:
* open /register
* enter "!hotmail@.com" into element ```#email```
* enter password with test_user's password into element ```#password```
* enter name with test_user' name into element ```#name```
* enter password2 with test_user's password into element ```#password2```
* click element ```input[type = "submit"]```
* open /login
* check that ```#message``` is "{} format is incorrect."
* Open /logout (clean up)

#### R2.9.2
* Mock backend.get_user to return a test_user instance
Actions:
* open /register
* enter email with test_user's email into element ```#email```
* enter "!@)#$(*@#$(!*@#)$*)@#($*)!)@(#$#(" into element ```#password```
* enter name with test_user' name into element ```#name```
* enter password2 with test_user's password into element ```#password2```
* click element ```input[type = "submit"]```
* open /login
* check that ```#message``` is "{} format is incorrect."
* Open /logout (clean up)

#### R2.9.3
* Mock backend.get_user to return a test_user instance
Actions:
* open /register
* enter email with test_user's email into element ```#email```
* enter password with test_user's password into element ```#password```
* enter "1234"into element ```#name```
* enter password2 with test_user's password into element ```#password2```
* click element ```input[type = "submit"]```
* open /login
* check that ```#message``` is "{} format is incorrect."
* Open /logout (clean up)

#### R2.9.4
* Mock backend.get_user to return a test_user instance
Actions:
* open /register
* enter email with test_user's email into element ```#email```
* enter password with test_user's password into element ```#password```
* enter name with test_user' name into element ```#name```
* enter "!@)#$(*@#$(!*@#)$*)@#($*)!)@(#$#(" into element ```#password2```
* click element ```input[type = "submit"]```
* open /login
* check that ```#message``` is "{} format is incorrect."
* Open /logout (clean up)

#### Test case R2.10 - If the email already exists, show message 'this email has been ALREADY used'
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /register
* enter test_user's email into element ```#email```
* check ```input[id = "email"]``` already exists
* check that ```#message``` is "this email has been ALREADY used"


#### Test case R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /register
* enter "test123@google.com" into element ```#email```
* enter "testing327" into element ```#password```
* enter "testing327" into element ```#password2```
* enter "tester327" into element #name
* click element ```input[type="submit"]```
* add 5000 into element ```#balance```
* open /login
* validate that 5000 value added to balance successfully. 
* Open /logout (clean up)

#### Test case R3.1 - If the user is not logged in, redirect to login page
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalid any logged-in sessions may exist)
* open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* open /login
* validate that current page shows (some element on the login page)
* Open /logout (clean up)

#### Test case R3.2 - This page shows a header 'Hi {}'.format(user.name)
Actions:
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalid any logged-in sessions may exist)
* open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* validate that current page shows ```#hi``` header
* Open /logout (clean up)

#### Test case R3.3 - This page shows user balance.
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* Open /logout (to invalid any logged-in sessions may exist)
* Open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* validate that current page shows ```#balance``` element
* Open /logout (clean up)

#### Test case R3.4 - This page shows a logout link, pointing to /logout
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* Open /logout (to invalid any logged-in sessions may exist)
* Open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* validate that current page shows ```#logout``` element
* validate that current page shows ```#logout``` element and points to ```#logout``` element 
* Open /logout (clean up)

#### Test case R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* Open /logout (to invalid any logged-in sessions may exist)
* Open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* validate that current page contains and lists  ```#all_tickets``` ,  ```#quantity_tickets```,  ```#email```,  ```#tickets_price``` and ```input[type="submit"]``` elements. 
* Open /logout (clean up)

#### Test case R3.6 - This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* Open /logout (to invalid any logged-in sessions may exist)
* Open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* Validate that the form element contains the  ```#name```,  ```#quantity_sell```,  ```#price_sell``` and ```#expirationdate_sell``` elements. 
* Open /logout (clean up)
