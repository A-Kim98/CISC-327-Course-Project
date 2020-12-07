# CISC 327 Course Project Design Document
Fall Quarter 2020

**CISC 327 Course Project Team:**<br>
Ahn, Jihoo<br>
Cole, Bram<br>
Kim, Alice<br> 

**Customer:**<br>
Steven Ding

**Table of Contents:**

1. Project Information
2. Techniques and Tools
3. Project Tasks
4. Budget Management
5. Architecture

## 1. Project Information
### 1.1. Purpose

This design document is for the project "CISC 327 Course Project", a Flask and Python-based web project for purchasing and selling tickets. This design document will contain the overall structure of the team's solution to create bug-free design of the project.

### 1.2. Test Coverage

This design document will cover the following scenarios:
- (R1) Log in process
- (R2) Registering process
- (R3) User profile page
- (R4) Ticket-selling process
- (R5) Ticket-updating process
- (R6) Ticket-buying process
- (R7) Log out process
- (R8) When user tries to access an invalid page

### 1.3. Overall Project Structure
Here is the overall control flow of the project:
![Project Structure](/assets/images/controlflows.png "Project Structure")

0. The actor is sent to the login page, /login
1. If the actor does not have an account, they will click on "Register"
    Otherwise, skip to step 5
2. In /register, the actor is able to type in information necessary to Register.
3. The actor presses "Register" button to complete registration. 
    They are able press "Login" to return to login page if they mistakenly came to this page when they have an account.
4. Whether registration is successful or unsuccessful, the actor is sent back to /login. If unsuccessful, error message will display, indicating the failure.
5. The actor is able to login now in /login by entering their email and password and pressing "Log In". 
6. The actor is now in the page / now, which contains their profile and other functions that enable them to buy, sell, and update tickets. On the page, there are other informations including the user's username, available balance, and tickets available for purchase.
7. By pressing on buy, sell, and update buttons after typing the desired ticket information in the respective forms, they are able to buy, sell, and update tickets.
8. Pressing logout will redirect the actor to the route /logout, removing all personal and ticket information from the actor, taking away permission to access / page from them, and sending the actor back to /login page again.

Functions to deposit money into the website and take money from the website were not requested by the customer.


## 2. Techniques and Tools
### 2.1 Communication among the Team

During the creation step of functions of the project, the team will communicate through a group chat to constantly update each other on functionality, clarity on instructions, specifications, and overall process of the project. And then, Github and pytest integration via Github Actions were used to ensure that any edits that any team member has made were integrated with the main project without flaws.

### 2.2 Communication with the Customer
With the customer, communication happens through either the customer's github page or Discord application in order to clarify any details of the project that may cause misunderstanding or ambiguity on the final desired product. Links to the pull requests made my development team members were occassionally sent to the customer so that the customer could check up on the process.

### 2.3 FrontEnd
We will be using Python language and Flask library in order to create the frontend. The codes for frontend will be in `frontend.py`.
Refer back to *1.3* - Overall Project Structure for a diagram of, and an explanation of what frontend of the proejct should do.
the frontend represents the view in the the model view controller design pattern
### 2.4 BackEnd
The solution for backend, which controls the business logics such as actions that involve transactions and data models' interactions, are written in `backend.py`. In the backend,  models will be called to interact with SQLite, a server-less database, to modify data.

![Project Structure](/assets/images/integrationtesting_architecture.png "Project Structure")
the backend represents the controller in the model view controller design pattern
### 2.5 Integration
By using SQLite, the program will run the front end during the day, backend during the night, and produce new data files the next day. Any conflicts at transaction will be left for customer services to resolve.


### 2.6 Deployment
Once the project is complete and it is ready to be published, docker files and cloud deployment will be used in order to properly allow the website to be visited by other users.

## 3. Project Tasks
### 3.1 Responsibilities
As of Nov. 4th, 2020, the responsibilities of test coverage sections are as followings:
| Jihoo 	| Design Doc    |
| Alice 	| R1, R2        |
| Bram  	| R3 	        |

### 3.2 Test Cases Priority
The priority will follow the following list:
1. R1 (login)
2. R7 (logout)
3. R2 (register)
4. R4 (sell)
5. R5 (update)
6. R6 (buy)
7. R3 (profile page)
8. R8 (non-existent page)

The reason is due to security reasons. If login, logout, or register pages' inputs are fumbled with, it can easily be led to a security issue, of allowing an intruder to check for security flaws in the login, logout, or register pages such as leaving user information vulnerable. This may cause security flaws such as an intruder logging in acting like a ticket owner, then updating the ticket to make the number undesirable for the original owner. Therefore, these pages were proritized. Then, sell, update, and buy were prioritized next as these require 

### 3.3 Test Case Organization
The website is relativily small and as it grows organization and the techniques used will change to scale with the amount of user's. Currently we will not test architecture as the architecture isn't particularly complicated yet. Each file with code in it that needs testing will have a corresponding file for unit tests. Other tests will have their own file(eg integration testing will have a file for all integration tests)

### 3.4 Tools Techniques and Standard's
**Tools:**
Selenium- for frontend testing. It will allow us to automate browsing and form entry.
Pytest- Our chosen testing framework
Github CI- will be used for regression testing

**Techniques:**
Unit tests will be written. Integration testing will currently be done by integrating the model, view and controller. Lower level integration testing can be preformed if deemed necessary. System testing will also be preformed. Acceptance testing will be done through beta testing. The client may also be satisfied with just using the program or may want a certain percentage of user satisfaction.

Robustness Testing- throw bad inputs and see what happens. Intentionally cause certain parts of the system to fail and see what happens(eg. server failure, database corruption) (this latter method may be deemed excessive if we haven't scaled much)
Documentation and Coding Style/Consistency- inspection and a linter(flake8) we will use Pytest framework to document results
security testing- do some penetration testing and then fix security wholes. We only need a small amount of deterrence for a small website. If the website grows more pen testing will be done done. 
Usability Testing- in the beta track how many tries it takes for the user to do some action
Compatibility Testing- test different resolutions and different machines. Virtual machines may be a good option to determine compatibility.

If we scale enough performance testing may be needed.

**Standards**
We will let the tester decide in which way they would like to test but they should adhere to some guidlines:
-the tester must attempt to maximize coverage.
-There are only 2000 github action minutes per month so the method to determine whether a test method is acceptable is described below
1. Calculate the number of test cases for the given methodology
2. Record the average time for 10 tests
3. if time*#ofTestCases > 1 minute you must rewrite the test

At some point if the website needs scaling then it would be acceptable to write code that automatically writes tests

Tester must describe--> inputs, actions/events, expected output, how we know the test is successful, expected coverage
These results must be documented somewhere
## 4. Budget Management
### 4.1 Test Cases
The team will use the above priority to filter out low-priority tasks and tests if budgets are running short or is calculated to be short when the budget is given.

## 5. Architecture
The init file defines global vars and config values. Main runs the flask app.

The frontend has routes that handle http requests. Each route has a method associated with either POST or GET. 
register_get() gets the template for the register page
register_post() ensures inputs entered into form are correct. Once correct they are registered with the database using a function from the controller.
login_get() gets the template for the login page
login_post() checks if a user exists with the form information using a session object. 
Sesssion is an object that contains sharing information between browser and the server. The user object is stored in session to tell if the client has logged in.
logout pops the logged_in attribute from session and redirects.
page_not_found() gives the template for a 404 error
authenticate will wrap around any function that accepts a user object and will check to if logged in. If not redirects to login.
returns a profile template and gets ticket info from controller this is where authentication is done
buy_ticket() checks if the user-provided the correct ticket information that they want to buy. If all the information is provided correctly, the user can buy the tickets. If not, redirects to the profile page with the error messages. 
update_ticket() checks if the user-provided the correct information they want to update, and if all the information is provided correctly, the user can update the ticket information. If not, redirects to the profile page with the error messages. 
sell_ticket() checks if the user-provided the correct information they want to sell, and if all the information is provided correctly, the user can successfully sell the tickets. If not, redirects to the profile page with the error messages. 

in the backend:
get_user queries the database for the user has email param
login_user checks for user authentifcation and has email and password params
register_user() registers the user to the database and accepts all params in the register page forms. It creates a user object with a balance of 5000
get_ticket() queries the database for the ticket that the user has. 
get_all_tickets() finds all the available tickets in the database. 
sell_ticket() takes the user and tickets information and sell the tickets based on the ticket information. 
get_update() takes user name as the input check if the ticket that user wants to update exists in the database. 

Model:
a class called user exists with id email password and names  as attributes
