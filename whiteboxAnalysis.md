# White box Analysis


#### Statement Coverage
To Start:
* Every Piece of Backend Code is run in the Frontend so as long as the frontend is covered we will have covered all of the code
* some of the tests are already written
* use a code coverage feature to determine statement coverage and write white box tests for statements not covered

System: Design a tests case to exercise each statement in the program

Completion: Test case for every line of code. Running a code coverage test will tell us if every line is covered
 
 I'm using pycharm IDE which has a code coverage feature. With the current tests we already have we cover 97 percent of the
 frontend code and 95% of the backend code. 
 
 
![Code Coverage Before Whitebox](/assets/images/coverageBefore.png)

The IDE will also highlight which code has not been covered.

![IDE highlighting a non covered else statment](/assets/images/highlightPycharm.png)

Here are the tests we need to write to cover all statments:
* A userName that is shorter than 3 charachters on register
* An incorrect email/password combo with proper formatting on login
* The empty ticket name code is also unreachable due to the please fill in this field popup
* validate_ticket_date had one line of unreachable code
* a valid date format but an expired date entry test
* A buy post with proper formatting that will buy all of a quantity of a ticket

We just need to make sure that these tests don't fail. 

The tests have been written and now we have covered all statments in the code.
