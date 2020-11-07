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

The actor, or the user, would be able to access login and register page at start, and then user homepage once they are logged in. To access user homepage with buying, selling, and accounting functions, they must be logged in - if only registered, the website will ask for log in once again. In the user homepage of the logged in actor, they will be given options to buy, sell, or update the ticket, as well as information on the actor's profile and account balance. 
Functions to deposit money into the website and take money from the website were not requested by the customer.


## 2. Techniques and Tools
### 2.1 Communication among the Team

During the creation step of functions of the project, the team will communicate through a group chat to constantly update each other on functionality, clarity on instructions, specifications, and overall process of the project. And then, Github and pytest integration via Github Actions were used to ensure that any edits that any team member has made were integrated with the main project without flaws.

### 2.2 Communication with the Customer
With the customer, communication happens through either the customer's github page or Discord application in order to clarify any details of the project that may cause misunderstanding or ambiguity on the final desired product. Links to the pull requests made my development team members were occassionally sent to the customer so that the customer could check up on the process.

### 2.3 FrontEnd
We will be using Python language and Flask library in order to create the frontend. The codes for frontend will be in `frontend.py`.
Refer back to *1.3* - Overall Project Structure for a diagram of, and an explanation of what frontend of the proejct should do.

### 2.4 BackEnd
The solution for backend, which controls the business logics such as actions that involve transactions and data models' interactions, are written in `backend.py`. In the backend,  SQL language will be used to allow the program to interact with SQLite, server-less database 

![Project Structure](/assets/images/integrationtesting_architecture.png "Project Structure")

### 2.5 Integration
By using SQLite, the program will run the front end during the day, backend during the night, and produce new data files the next day. Any conflicts at transaction will be left for customer services to resolve.

![Project Structure](/assets/images/architecture.png "Project Structure")

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


## 4. Budget Management
### 4.1 Test Cases
The team will use the above priority to filter out low-priority tasks and tests if budgets are running short or is calculated to be short when the budget is given.