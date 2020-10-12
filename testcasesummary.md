| Targeted part of  specifications | Test case ID | Purpose of Test Case                                                                                                                                                |
|----------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R3.7                             | R3.7         | To test if the form to submit new tickets to sell exists, and if it has all the fields required: name, quantity, price, expiration date                             |
| R3.8                             | R3.8         | Testing if ticket-selling form's sell button redirects to the /sell route                                                                                           |
| R3.9                             | R3.9         | Testing if ticket-buying form's buy button redirects to the /buy route                                                                                              |
| R3.10                            | R3.10        | Testing if ticket-update form's update button redirects to the /update button                                                                                       |
| R4.1                             | R4.1.1       | Testing to make sure the name field of the ticket-selling form cannot contain non-alphanumerical characters                                                         |
|                                  | R4.1.2       | Testing to make sure the name field of the ticket-selling form cannot begin with a space                                                                            |
|                                  | R4.1.3       | Testing to make sure the name field of the ticket-selling form cannot end with a space                                                                              |
| R4.2                             | R4.2         | Testing to make sure the name field of the ticket-selling form cannot be longer than 60 characters                                                                  |
| R4.3                             | R4.3.1       | Testing to make sure the quantity field of the ticket-selling form cannot be 0 or below                                                                             |
|                                  | R4.3.2       | Testing to make sure the quantity field of the ticket-selling form cannot be exceeding 100                                                                          |
| R4.4                             | R4.4.1       | Testing to make sure the price field of the ticket-selling form cannot be under 10                                                                                  |
|                                  | R4.4.2       | Testing to make sure the price field of the ticket-selling form cannot be exceeding 100                                                                             |
| R4.5                             | R4.5         | Testing to make sure the date field of the ticket-selling form has to be in YYYYMMDD format                                                                         |
| R4.6                             | R4.6         | Testing if any error redirects back to / (user profile) and shows an error message                                                                                  |
| R4.7                             | R4.7         | Testing to make sure when a form to sell a ticket is submitted, it is posted on the user profile page                                                               |
| R5.1                             | R5.1.1       | Testing to make sure the name field of the ticket-buying form cannot contain non-alphanumerical characters                                                          |
|                                  | R5.1.2       | Testing to make sure the name field of the ticket-buying form cannot begin with a space                                                                             |
|                                  | R5.1.3       | Testing to make sure the name field of the ticket-buying form cannot end with a space                                                                               |
| R5.2                             | R5.2         | Testing to make sure the name field of the ticket-buying form cannot be longer than 60 characters                                                                   |
| R5.3                             | R5.3.1       | Testing to make sure the quantity field of the ticket-buying form cannot be 0 or below                                                                              |
|                                  | R5.3.2       | Testing to make sure the quantity field of the ticket-buying form cannot be exceeding                                                                               |

Describing the test plan:
 Q. How did your team organize the documentations of the test cases?
 A. We have decided to name our testcases testcases1, testcases2, testcases3 and put them in the same place.

 Q. Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub?
 A. A sample of what we wanted the page to look like was made via photoshop, where we wanted to have a table in the user profile and forms for buying, selling, and updating a ticket below, where the elements for name of, say, buying form, selling form, update form would be called #name_buy, #name_sell, and #name_update respectively.

 Q. How are you going to organize different test case code files? (a folder for a specification?)
 A. Undecided