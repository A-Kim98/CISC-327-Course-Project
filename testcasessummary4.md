| Targeted part of   specifications | Test Case ID | Purpose of Test Case                                                         |
|-----------------------------------|--------------|------------------------------------------------------------------------------|
| R5.0                              | R5.0.1       | positive test case validation(quantity 1 and price 10)                       |
|                                   | R5.1.1       | positive test case validation(quantity 100 and price 100)                    |
| R5.1                              | R5.1.1       | validate that a non-alpha numeric is rejected                                |
|                                   | R5.1.2       | validate that space as first character is rejected                           |
|                                   | R5.1.3       | validate that space as last    character is rejected                         |
| R5.2                              | R5.2.1       | check that something longer than 60 characters is accepted                   |
| R5.3                              | R5.3.1       | check that a quantity of zero is rejected                                    |
|                                   | R5.3.2       | check that a quantity greater than 100 is rejected                           |
| R5.4                              | R5.4.1       | check price rejects a price of 9                                             |
|                                   | R5.4.2       | check price rejects a price of 101                                           |
| R5.5                              | R5.5.1       | check that invalid input in date field is rejected                           |
| R5.6                              | R5.6.1       | ensure a non existant ticket is rejected                                     |
| R5.7                              | R5.7.1       | ensure errors show an error message on user home page                        |
| R6.4                              | R6.4.1       | ensure a ticket that does not exist is rejected                              |
|                                   | R6.4.2       | ensure that users cannot buy more tickets than that which is offered         |
| R6.5                              | R6.5.1       | ensure that if the user does not have enough balance the input is   rejected |
| R6.6                              | R6.6.1       | ensure errors show an error message on user home page                        |
| R7.1                              | R7.1.1       | ensure logout redirects to logout page                                       |
|                                   | R7.1.2       | ensure that user cannot access the user home page                            |
| R8.1                              | R8.1         | ensure a 404 will show up for an invalid input                               |
