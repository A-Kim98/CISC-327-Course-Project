# Front End Requirements: Test Cases Page 4

Test data:  
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
    balance = 1400
)
```
```
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='t 1',
    quantity=10,
    price=100,
    date='20200901'
)
```
#### Test case R5.0.1 - Checking for positive case for the fields of ticket's updating form
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter test_ticket's name into element ```#name_update```
* Enter the value ```1``` into element ```#quantity_update```
* Enter the value ```10``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Validate that the ```#message``` does not equal to "Ticket name must be alphanumeric-only"
* Validate that the ```#message``` does not equal to "Ticket name cannot begin with a space"
* Validate that the ```#message``` does not equal to "Ticket name cannot end with a space"
* Validate that the ```#message``` does not equal to "Ticket name cannot be longer than 60 characters"
* Validate that the ```#message``` does not equal to "At least one ticket must be purchased"
* Validate that the ```#message``` does not equal to "At most 100 tickets can be purchased"
* Validate that the ```#message``` does not equal to "Ticket price must be 10 dollars or above"
* Validate that the ```#message``` does not equal to "Ticket price must be lower than 100 dollars"
* Validate that the ```#message``` does not equal to "Expiration date is in invalid format"
* Validate that the ```#message``` does not equal to "The ticket does not exist"
* Open /logout (clean up)

#### Test case R5.0.1 - Checking for positive case for the fields of ticket's updating form - upper boundaries
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter test_ticket's name into element ```#name_update```
* Enter the value ```100``` into element ```#quantity_update```
* Enter the value ```100``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Validate that the ```#message``` does not equal to "Ticket name must be alphanumeric-only"
* Validate that the ```#message``` does not equal to "Ticket name cannot begin with a space"
* Validate that the ```#message``` does not equal to "Ticket name cannot end with a space"
* Validate that the ```#message``` does not equal to "Ticket name cannot be longer than 60 characters"
* Validate that the ```#message``` does not equal to "At least one ticket must be purchased"
* Validate that the ```#message``` does not equal to "At most 100 tickets can be purchased"
* Validate that the ```#message``` does not equal to "Ticket price must be 10 dollars or above"
* Validate that the ```#message``` does not equal to "Ticket price must be lower than 100 dollars"
* Validate that the ```#message``` does not equal to "Expiration date is in invalid format"
* Validate that the ```#message``` does not equal to "The ticket does not exist"
* Open /logout (clean up)

#### Test case R5.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
#### Test case R5.1.1 - Check if name of the ticket is alphanumeric-only and space allowed in middle
Mocking:
* Mock backend.get_user to return a test_user instance


Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1&t2@!*")(/.,<>[]-+``` into element ```#name_update```
* Enter the value ```1``` into element ```#quantity_update```
* Enter the value ```15``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Check that ```#message``` is "Ticket name must be alphanumeric-only"
* Open /logout (clean up)

#### Test case R5.1.2 - Check space is not allowed as first character
Mocking:
* Mock backend.get_user to return a test_user instance


Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ``` t1``` into element ```#name_update```
* Enter the value ```1``` into element ```#quantity_update```
* Enter the value ```15``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Check that ```#message``` is "Ticket name cannot begin with a space"
* Open /logout (clean up)

#### Test case R5.1.3 - Check space is not allowed as last character
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1 ``` into element ```#name_update```
* Enter the value ```1``` into element ```#quantity_update```
* Enter the value ```15``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Check that ```#message``` is "Ticket name cannot end with a space"
* Open /logout (clean up)

#### Test case R5.2.1 - The name of the ticket is no longer than 60 characters
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:  
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghi``` into element ```#name_update```
* Enter the value ```1``` into element ```#quantity_update```
* Enter the value ```15``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Check that ```#message``` is "Ticket name cannot be longer than 60 characters"
* Open /logout (clean up)

#### Test case R5.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100.
### Test case R5.3.1 - The quantity of the tickets has to be more than 0 - negative
Mocking:
* Mock backend.get_user to return a test_user instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1```` into element ```#name_update```
* Enter the value ```0``` into element ```#quantity_update```
* Enter the value ```15``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Check that ```#message``` is "At least one ticket must be purchased"
* Open /logout (clean up)

#### Test case R5.3.2 - The quantity of the tickets has to be less than or equal to 100 -negative
Mocking:
* Mock backend.get_user to return a test_user instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_update```
* Enter the value ```101``` into element ```#quantity_update```
* Enter the value ```15``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Check that ```#message``` is "At most 100 tickets can be purchased"
* Open /logout (clean up)


#### Test case R5.4 - Price has to be of range [10, 100]

#### Test case R5.4.1 - boundary of 10 - negative
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:  
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* Enter ```9``` into element ```#price_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that #message is "Ticket price must be 10 dollars or above"
* Open /logout (clean up)

#### Test case R5.4.2 - boundary of 100 - negative
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:  
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* Enter ```101``` into element ```#price_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that #message is "Ticket price must be lower than 100 dollars"
* Open /logout (clean up)

#### Test case R5.5.1: - Date must be given in the format YYYYMMDD (e.g. 20200901)

Mocking:
* Mock backend.get_user to return a test_user instance

Actions: 
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* enter test_user's email into element ```#email```
* enter test_user's password into element ```#password```
* click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_update```
* Enter the value ```1``` into element ```#quantity_update```
* Enter the value ```101``` into element ```#price_update```
* Enter the value ```Sept. 9 2021``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Check that ```#message``` is "Expiration date is in invalid format"
* Open /logout (clean up)


#### Test case R5.6.1: - The ticket of the given name must exist - Negative
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```this ticket does not exist``` into element ```#name_update```
* Enter the value ```2``` into element ```#quantity_update```
* Enter the value ```15``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Check that ```#message``` is "The ticket does not exist"
* Open /logout (clean up)

#### Test case R5.7.1: - For any errors, redirect back to / and show an error message
Mocking:
* Mock backend.get_user to return a test_user instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_update```
* Enter the value ```1``` into element ```#quantity_update```
* Enter the value ```101``` into element ```#price_update```
* Enter the value ```Sept. 9 2021``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Validate that current page redirects to the user profile page and contains header element ```'Hi {}'.format(user.name)```
* Validate that ```#message``` is not blank
* Open /logout (clean up)



#### Test case R6.4: - The ticket name exists in the database and the quantity is more than the quantity requested to buy

#### Test case R6.4.1: - The ticket name exists in the database - negative
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter the value ```this ticket does not exist``` into element ```#name_buy```
* Enter test_ticket's quantity into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Check that ```#message``` is "Ticket not found"
* Open /logout (clean up)

#### Test case R6.4.2: - The ticket quantity is more than the quantity bought - negative
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter test_ticket's name into element ```#name_buy```
* Enter the value ```11``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Check that ```#message``` is "The quantity exceeds the quantity of tickets for sale"
* Open /logout (clean up)

#### Test case R6.5.1: - The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) (in this case it is 1400$ assuming tax before service fee)- negative
Test data:  
```
test_user_neg = User(
    email='test_frontend_neg@test.com',
    name='test_frontend_neg',
    password=generate_password_hash('test_frontend_neg')
    balance=1399
)
```
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* open /logout (to invalidate any logged in sessions may exist)
* open /login
* Enter test_user_neg's email into element #email
* Enter test_user_neg's password into element #password
* Click element ```input[type="submit"]```
* Enter test_ticket's name into element ```#name_buy```
* Enter the value ```10``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Check that ```#message``` is "Not enough money for ticket purchase"
* Open /logout (clean up)

#### Test case R6.6.1: - 	For any errors, redirect back to / and show an error message
Mocking:
* Mock backend.get_user to return a test_user instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_buy```
* Enter the value ```1``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Validate that current page redirects to the user profile page and contains header element ```'Hi {}'.format(user.name)```
* Validate that ```#message``` is not blank
* Open /logout (clean up)


#### Test case R7.1: - 	Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.
#### Test case R7.1.1: - 	Logout will invalid the current session and redirect to the login page.
Mocking:
* Mock backend.get_user to return a test_user instance

Actions: 
* open /logout (ensure the user will properly log in and invalidate unwanted session)
* open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* open /logout
* validate that the current page has a ```h1``` element containing ```Log In```
* Open /logout (clean up)

#### Test case R7.1.2: - 	After logout, the user shouldn't be able to access restricted pages.
Mocking:
* Mock backend.get_user to return a test_user instance

Actions: 
* open /logout (ensure the user will properly log in and invalidate unwanted session)
* attempt to open /
* validate that the current page has a ```h1``` element containing ```Log In```
* Open /logout (clean up)

#### Test case R8.1: - For any other requests except the ones above, the system should return a 404 error
Actions: 
* open /thisPageDoesNotExist
* validate that the current page has a ```p``` element containing ```The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.```
* Open /logout (clean up)

