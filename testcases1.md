# Front End Requirements: Test Cases Page 1

Test data:  
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

#### Test case R1.1 - If the user hasn't logged in, show the login page
Actions:  
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* validate that the current page has a ```h1``` element containing ```Log In```

#### Test case R1.2: the login page has a message that by default says 'please login'
Actions: 
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* validate that the ```#message``` element contains the text "please login"

#### Test case R1.3: If the user has logged in, redirect to the user profile page 
Mocking:

* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalid any logged-in sessions may exist)
* open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* open /login again
* validate that current page contains ```#welcome-header``` element

#### Test case R1.4 -The login page provides a login form which requests two fields: email and passwords
Actions: 
* open /login
* validate that the element ```#email``` exists
* validate that the element ```#password``` exists

#### Test case R1.5 - The login form can be submitted as a POST request to the current URL (/login)
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalid any logged-in sessions may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element ```input[type="submit"]```
* validate that you got redirected to / which contains ```#welcome-header``` element

#### Test case R1.6 - Email and password both cannot be empty
Mocking:
* Mock backend.get_user to return a test_user instance
#####R1.6.1
Actions: 
* open /login
* enter test_user's email into element ```#email```
* leave test_user's password blank and click ```input[type="submit"]```
* validate that you receive error ```#message``` "Email and/or password cannot be empty"
#####R1.6.2
Actions: 
* open /login
* enter test_user's email into element ```#password```
* leave test_user's email blank and click ```input[type="submit"]```
* validate that you receive error ```#message``` "Email and/or password cannot be empty"
#####R1.6.3
Actions: 
* open /login
* leave test_user's email and password blank and click ```input[type="submit"]```
* validate that you receive error ```#message``` "Email and/or password cannot be empty"

#### Test case R1.7 - Email has to follow addr-spec defined in RFC 5322
##### R1.7.1
Actions: 
* open /login
* input ```1234567890123456789012345678901234567890123456789012345678901234+x@example.com``` into element ```#email```
* input a password in element ```#password```
* click element ```input[type = "submit"]```
* check that ```#message``` is "email/password format is incorrect."

##### R1.7.2
Actions: 
* open /login
* input ```abc.example.com``` into element ```#email```
* input a password in element ```#password```
* click element ```input[type = "submit"]```
* check that ```#message``` is "email/password format is incorrect."

##### R1.7.3
Actions: 
* open /login
* input ```a"b(c)d,e:f;g<h>i[j\k]l@example.com``` into element ```#email```
* input a password in element ```#password```
* click element ```input[type = "submit"]```
* check that ```#message``` is "email/password format is incorrect."

##### R1.7.4
Actions: 
* open /login
* input ```i_like_underscore@but_its_not_allow_in_this_part.example.com``` into element ```#email```
* input a password in element ```#password```
* click element ```input[type = "submit"]```
* check that ```#message``` is "email/password format is incorrect."

#### Test case R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character

##### R1.8.1
Actions: 
* open /login
* input test_user's email into ```#email```
* input a password "test!" 
* click element ```input[type = "submit"]```
* check  element ```#pwmessage``` is "Password needs minimum length 6, at least one upper case, at least one lower case, and at least one special character." (needs minimum length 6)
##### R1.8.2
Actions: 
* open /login
* input test_user's email into ```#email```
* input a password "test123! 
* click element ```input[type = "submit"]```
* check element ```#pwmessage``` is "Password needs minimum length 6, at least one upper case, at least one lower case, and at least one special character." (needs at least one upper case)
##### R1.8.3
Actions: 
* open /login
* input test_user's email into ```#email```
* input a password "TEST123!"
* click element ```input[type = "submit"]```
* check element ```#pwmessage``` is "Password needs minimum length 6, at least one upper case, at least one lower case, and at least one special character."  (needs at least one lower case)
##### R1.8.4
Actions: 
* open /login
* input test_user's email into ```#email```
* input a password "TESt123" 
* click element ```input[type = "submit"]```
* check element ```#pwmessage``` is "Password needs minimum length 6, at least one upper case, at least one lower case, and at least one special character."  (needs at least one special character)

#### Test case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
Actions:
* open /login
* enter email with formatting error into element ```#email```
* enter password with formatting error into element #password
* click element ```input[type = "submit"]```
* check that ```#message``` is "email/password format is incorrect"

#### Test case R1.10 - If email/password are correct, redirect to /

Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalid any logged-in sessions may exist)
* open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* open /login again
* validate that current page contains ```#welcome-header``` element

#### Test case R1.11-Otherwise, redirect to /login and show message 'email/password combination incorrect'
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalid any logged-in sessions may exist)
* open /login
* enter incorrect email eg.```wrongemail@test.com``` into element ```#email```
* enter incorrect password eg.```wrongpassword!``` into element ```#password```
* click element ```input[type="submit"]```
* open /login again
* validate that ```#message``` is ''email/password combination incorrect''

#### Test case R2.1 If the user has logged in, redirect back to the user profile page /
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalid any logged-in sessions may exist)
* open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* open /register
* validate that current page redirects to the user page and contains ```#welcome-header``` element

#### Test case R2.2- Show the user registration page if user is not logged in

Actions:
* open /logout (to invalid any logged-in sessions may exist)
* open /register
* validate that the ```h1``` element contains ```Register```

#### Test case R2.3 - The registration page shows a registration form requesting: email, user name, password, password2
Actions:
* open /register
* check that the page contains element ```#email```
* check that the page contains element ```#name```
* check that the page contains element ```#password```
* check that the page contains element ```#password2```

#### Test case R2.4 - The registration form can be submitted as a POST request to the current URL (/register)
Actions:
* open /register
* enter test_user's email into element ```#email```
* enter test_user's name into element ```#name```
* enter test_user's password into element ```#password```
* enter test_user's password into element ```#password2```
* click element ```input[type="submit"]```
* open /register
* validate that current page redirects to the login page and contains ```h1``` element with the text  ```Login```