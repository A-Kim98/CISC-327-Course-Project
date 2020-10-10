# CISC-327-Course-Project

#### Test case R2.5 - Email, password, password2 all have to satisfy the same required as defined in R1
Actions:
* open /register
* check that ```#email```, ```#password``` and ```#password2``` are not empty
* check that ```#email``` follows addr-spec defined in RFC 5322
* check that ```#password``` meet the required complexity

#### Test case R2.6 - Password and password2 have to be exactly the same
Actions:
* open /register
* check that content of ```#password``` and ```#password2``` are equal

#### Test case R2.7 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.

#### R2.7.1
Actions:
* open /register
* input test_user's email into ```#email```
* input test_user's password into ```#password```
* input a user name ""
* click element ```input[type = "submit"]```
* check element #name_error1 is "User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character."

#### R2.7.2
Actions:
* open /register
* input test_user's email into ```#email```
* input test_user's password into ```#password```
* input a user name "1234"
* click element ```input[type = "submit"]```
* check element #name_error1 is "User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character."

#### R2.7.3
Actions:
* open /register
* input test_user's email into ```#email```
* input test_user's password into ```#password```
* input a user name " testuser"
* click element ```input[type = "submit"]```
* check element ```#name_error1``` is "User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character."

#### R2.7.4
Actions:
* open /register
* input test_user's email into ```#email```
* input test_user's password into ```#password```
* input a user name "testuser "
* click element ```input[type = "submit"]```
* check element ```#name_error1``` is "User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character."

#### Test case R2.8 - User name has to be longer than 2 characters and less than 20 characters.
#### R2.8.1
Actions:
* open /register
* input test_user's email into ```#email```
* input test_user's password into ```#password```
* input a user name "a"
* click element ```input[type = "submit"]```
* check element ```#name_error2``` is "User name has to be longer than 2 characters and less than 20 characters."

#### R2.8.2
Actions:
* open /register
* input test_user's email into ```#email```
* input test_user's password into ```#password```
* input a user name "Polytetrafluoroethylene" into ```#name```
* click element ```input[type = "submit"]```
* check element ```#name_error2``` is "User name has to be longer than 2 characters and less than 20 characters."

#### Test case R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)
Actions:
* open /register
* enter email with formatting error into element ```#email```
* enter password with formatting error into element ```#password```
* enter name with formatting error into element ```#name```
* enter password2 with formatting error into element ```#password2```
* open /login
* check that ```#message``` is "{} format is incorrect.".format(the_corresponding_attribute)

#### Test case R2.10 - If the email already exists, show message 'this email has been ALREADY used'
Actions:
* open /register
* enter test_user's email into element ```#email```
* check ```input[id = "email"]``` exists
* check that ```#message``` is "this email has been ALREADY used"

#### Test case R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
Actions:
* open /register
* enter "test123@google.com" into element ```#email```
* enter "testing327" into element ```#password```
* enter "testing327" into element ```#password2```
* enter "tester123" into element #name
* click element ```input[type="submit"]```
* add 5000 into element ```#balance```
* open /login

#### Test case R3.1 - If the user is not logged in, redirect to login page
Actions:
* open /logout (to invalid any logged-in sessions may exist)
* open /login
* validate that the current page has a h1 element containing Log In
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```

#### Test case R3.2 - This page shows a header 'Hi {}'.format(user.name)
Actions:
* validate that current page contains ```#hi-header``` element

#### Test case R3.3 - This page shows user balance.
Actions:
* validate that current page contains ```#balance``` element

#### Test case R3.4 - This page shows a logout link, pointing to /logout
Actions:
* validate that current page contains ```#logout``` element
* check the ```#logout``` works
* open /logout

#### Test case R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
Actions:
* validate that current page contains ```#all_tickets``` element
* validate that current page contains ```#quantity_tickets``` element
* validate that current page contains ```#email``` element
* validate that current page contains ```#tickets_price``` element
* validate that current page contains ```input[type="submit"]``` element

#### Test case R3.6 - This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date
Actions:
* validate that the element ```form[method = "post"]``` exists
* validate that current page contains ```#name``` element
* validate that current page contains ```#quantity``` element
* validate that current page contains ```#price``` element
* validate that current page contains ```#expiration_date``` element
