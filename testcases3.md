# Front End Requirements: Test Cases Page 3

Test data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

test_tickets = [
    {'name': 't1', 'price': '100'}
]
```

#### Test case R3.7 - This page contains a form that a user can buy new tickets. Fields: name, quantity
Mocking:
* Mock backend.get_user to return a test_user instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Validate that the ```form```  element that contains the elements ```#name_buy``` and the element ```#quantity_buy``` exists

#### Test case R3.8 - The ticket-selling form can be posted to /sell
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter test_tickets' element 0's 'name' into element ```#name```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Validate that the current route is /sell

#### Test case R3.9 - The ticket-buying form can be posted to /buy
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter test_tickets' element 0's 'name' into element ```#name_buy```
* Enter the value ```1``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Validate that the current route is /buy

#### Test case R3.10 - The ticket-update form can be posted to /update
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter test_tickets' element 0's 'name' into element ```#name_update```
* Enter the value ```1``` into element ```#quantity_update```
* Enter the value ```15``` into element ```#price_update```
* Enter the value ```20210901``` into element ```#expdate_update```
* Click element ```input[type="submit" value="Update"]```
* Validate that the current route is /update

#### Test case R4.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

#### Test case R4.1.1 - Check if name of the ticket is alphanumeric-only
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1&t2@!*")(/.,<>[]-+``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that ```#message``` is "Ticket name must be alphanumeric-only"

#### Test case R4.1.2 - Check space is not allowed as first character
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ``` t1``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that ```#message``` is "Ticket name cannot begin with a space"

#### Test case R4.1.3 - Check space is not allowed as last character
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1 ``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that ```#message``` is "Ticket name cannot end with a space"

#### Test case R4.2 - The name of the ticket is no longer than 60 characters
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that ```#message``` is "Ticket name cannot be longer than 60 characters"

#### Test case R4.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100.

#### Test case R4.3.1 - The quantity of the tickets has to be more than 0
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1```` into element ```#name_sell```
* Enter the value ```0``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that ```#message``` is "At least 1 ticket must be purchased"

#### Test case R4.3.2 - The quantity of the tickets has to be less than or equal to 100
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that ```#message``` is "At most 100 tickets can be purchased"

#### Test case R4.4 - Price has to be of range [10, 100]

#### Test case R4.4.1 - Price cannot be lower than 10
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```9``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that ```#message``` is "Price of the ticket cannot be below 10"

#### Test case R4.4.2 - Price cannot be higher than 100
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```101``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that ```#message``` is "Price of the ticket cannot be below 10"

#### Test case R4.5 - Date must be given in the format YYYYMMDD (e.g. 20200901)
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```101``` into element ```#price_sell```
* Enter the value ```Sept. 9 2021``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Check that ```#message``` is "Expiration date is in invalid format"


#### Test case R4.6 - For any errors, redirect back to / and show an error message
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```101``` into element ```#price_sell```
* Enter the value ```Sept. 9 2021``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Validate that current page redirects to the user profile page and contains header element ```'Hi {}'.format(user.name)```

#### Test case R4.7 - The added new ticket information will be posted on the user profile page
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_sell```
* Enter the value ```1``` into element ```#quantity_sell```
* Enter the value ```15``` into element ```#price_sell```
* Enter the value ```20210901``` into element ```#expdate_sell```
* Click element ```input[type="submit" value="Sell"]```
* Validate that the element ```table``` contains the new ticket data:
```
<tr>
  <th>t1</th>
  <th>1</th>
  <th>15</th>
  <th>20210901</th>
</tr>
```

#### Test case R5.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

#### Test case R5.1.1 - The name of the ticket has to be alphanumeric-only
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1&t2@!*")(/.,<>[]-+``` into element ```#name_buy```
* Enter the value ```1``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Check that ```#message``` is "Ticket name must be alphanumeric-only"

#### Test case R5.1.2 - The name of the ticket cannot have space as first character
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ``` t1``` into element ```#name_buy```
* Enter the value ```1``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Check that ```#message``` is "Ticket name cannot begin with a space"

#### Test case R5.1.2 - The name of the ticket cannot have space as first character
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1 ``` into element ```#name_buy```
* Enter the value ```1``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Check that ```#message``` is "Ticket name cannot end with a space"

#### Test case R5.2 - The name of the ticket is no longer than 60 characters
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg``` into element ```#name_buy```
* Enter the value ```1``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Check that ```#message``` is "Ticket name cannot be longer than 60 characters"

#### Test case R5.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100.

#### Test case R5.3.1 - The quantity of the tickets has to be more than 0
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_buy```
* Enter the value ```0``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Check that ```#message``` is "At least one ticket must be purchased"

#### Test case R5.3.2 - The quantity of the tickets has to be less than or equal to 100
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_tickets to return a test_tickets instance

Actions: 
* Open /logout (to invalid any logged-in sessions that may exist)
* Open /login
* Enter test_user's email into element #email
* Enter test_user's password into element #password
* Click element ```input[type="submit"]```
* Enter ```t1``` into element ```#name_buy```
* Enter the value ```101``` into element ```#quantity_buy```
* Click element ```input[type="submit" value="Buy"]```
* Check that ```#message``` is "At most 100 tickets can be purchased"