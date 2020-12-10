from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn
import re  # regular expressions
import string
from datetime import datetime

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""


# TODO error messages are usually handled using try except blocks not if statments condider changing for clarity

@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


# The registration form can be submitted as a POST request to the current URL (/register)
@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    user = bn.get_user(email)
    error_message = None

    # validate email
    check_email = validate_email(email, error_message, user)

    # validate password and password2
    check_pwd = validate_password(password, password2, error_message)

    # validate username
    check_name = validate_username(name, error_message)

    '''
    validate user informations
        #if there is any error messages when registering new user
        # at the backend, go back to the register page.
    '''
    # email
    if check_pwd == "" and check_name == "":
        if check_email != "":
            return render_template('register.html', message=check_email)

    if check_pwd == "" or check_name == "":
        if check_email != "":
            return render_template('register.html', message=check_email)

    # password
    if check_email == "" and check_name == "":
        if check_pwd != "":
            return render_template('register.html', message=check_pwd)

    # name
    if check_email == "" and check_pwd == "":
        if check_name != "":
            return render_template('register.html', message=check_name)

    # fail to store
    if not bn.register_user(email, name, password, password2):
        error_message = "Failed to store user info."

    # If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
    if check_email == "" and check_pwd == "" and check_name == "":
        return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


# The login form can be submitted as a POST request to the current URL (/login)
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    error_message = None
    user = bn.login_user(email, password)
    # validate email
    check_email = validate_login_email(email, error_message, user)

    # validate password and password2
    check_pwd = validate_login_password(password, error_message)

    # For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
    # email
    if check_pwd == "":
        if check_email != "":
            return render_template('login.html', message=check_email)
    # password
    if check_email == "":
        if check_pwd != "":
            return render_template('login.html', message=check_pwd)

    if check_pwd != "" and check_pwd != "":
        if check_pwd == check_email:
            return render_template('login.html', message=check_email)

    if check_email == "" and check_pwd == "" and user:
        session['logged_in'] = user.email
        return redirect('/', code=303)

    # Otherwise, redict to /login and show message 'email/password combination incorrect'
    else:
        return render_template('login.html', message="email/password combination incorrect.")


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)


@app.route('/sell', methods=['POST'])
def sell_ticket():
    email = session['logged_in']
    user = bn.get_user(email)
    ticket_name = request.form.get('name_sell')
    ticket_quantity = int(request.form.get('quantity_sell'))
    ticket_price = int(request.form.get('price_sell'))
    ticket_date = request.form.get('expdate_sell')
    error_message = ""
    error_list = []
    # validate ticket name
    error_list.append(validate_ticket_name(ticket_name, error_message))

    # validate ticket quantity
    error_list.append(validate_ticket_quantity(ticket_quantity, error_message))

    # validate ticket price
    error_list.append(validate_ticket_price(ticket_price, error_message))

    # validate ticket date
    error_list.append(validate_ticket_date(ticket_date, error_message))

    # For any errors, redirect back to / and show an error message
    tickets = bn.get_all_tickets()
    print(error_list[0])
    if error_list[0] != "":
        return render_template('index.html', user=user, sell_message=error_list[0], tickets=tickets)
    elif error_list[1] != "":
        return render_template('index.html', user=user, sell_message=error_list[1], tickets=tickets)
    elif error_list[2] != "":
        return render_template('index.html', user=user, sell_message=error_list[2], tickets=tickets)
    elif error_list[3] != "":
        return render_template('index.html', user=user, sell_message=error_list[3], tickets=tickets)
    # The added new ticket information will be posted on the user profile page
    else:
        bn.sell_ticket(user, ticket_name, ticket_quantity, ticket_price, ticket_date)
        tickets = bn.get_all_tickets()
        return render_template('index.html', user=user, tickets=tickets)


@app.route('/update')
def update_ticket(user):
    ticket_name = request.form.get('name_update')
    ticket_quantity = request.form.get('quantity_update')
    ticket_price = request.form.get('price_update')
    ticket_date = request.form.get('expdate_update')
    ticket = bn.get_ticket(ticket_name)
    error_message = ""

    # validate ticket name
    check_ticket_name = validate_ticket_name(ticket_name, error_message)

    # validate ticket quantity
    check_ticket_quantity = validate_ticket_quantity(ticket_quantity, error_message)

    # validate ticket price
    check_ticket_price = validate_ticket_price(ticket_price, error_message)

    # validate ticket date
    check_ticket_date = validate_ticket_date(ticket_date, error_message)

    # vadliate ticket existence
    if ticket is None:
        error_message = "The ticket of the given name must exist"

    # for any errors, redirect back to / and show an error message
    if error_message != "":
        return redirect('/', update_message=error_message)


@app.route('/buy')
def buy_ticket(user):
    ticket_name = request.form.get('name_buy')
    ticket_quantity = request.form.get('quantity_buy')
    ticket = bn.get_ticket(ticket_name)
    error_message = ""

    # validate ticket name
    check_ticket_name = validate_ticket_name(ticket_name, error_message)

    # validate ticket quantity
    check_ticket_quantity = validate_ticket_quantity(ticket_quantity, error_message)

    # validate the ticket quantity in the database
    if ticket.quantity > ticket_quantity:
        error_message = "The ticket name exists in the database and the quantity is more than the quantity requested to buy"

    # Validate user balance
    if user.balance < (ticket.price * ticket_quantity * 0.35 * 0.05):
        error_message = "The user has less balance than the ticket price * quantity + service fee (35%) + tax (5%)"

    # for any errors, redirect back to / and show an error message
    if error_message != "":
        return redirect('/', buy_message=error_message)
    else:
        user.ticket.append(ticket)
        ticket = bn.get_all_tickets()
        return render_template('/', user=user, ticket=ticket)


'''
Validate email complexity and possible email format errors
# Email, password, password2 all have to satisfy the same required as defined in R1
# Email and password both cannot be empty
# Email has to follow addr-spec defined in RFC 5322
# If the email already exists, show message 'this email has been ALREADY used'

'''


def validate_email(email, error_message, user):
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if len(email) <= 1:
        error_message = "Email and/or password cannot be empty."

    else:
        if not re.search(email_regex, email):
            error_message = "Email/password format is incorrect."

        elif len(email) > 30:
            error_message = "Email/password format is incorrect."

        elif user:
            error_message = "This email has been ALREADY used."

        else:
            error_message = ""
    return error_message


'''
Validate password complexity and possible password/password2 format error
# Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
'''


def validate_password(password, password2, error_message):
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
    password_check = re.compile(password_regex)

    if len(password) <= 1 or len(password2) <= 1:
        error_message = "Email and/or password cannot be empty."

    elif (len(password) < 6 or len(password2) < 6) or (len(password) < 6 and len(password2) < 6):
        error_message = "Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character."

    else:
        if (not re.search(password_check, password)) and password == password2:
            error_message = "Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character."

        elif (not re.search(password_check, password)) or (not re.search(password_check, password2)):
            error_message = "Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, at least one special character and password and password2 have to be exactly the same."

        else:
            error_message = ""
    return error_message


'''
Validate user's email (login)
# If email/password are correct, redirect to /
'''


def validate_login_email(email, error_message, user):
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email_check = re.compile(email_regex)

    if len(email) <= 1:
        error_message = "Email and/or password cannot be empty."
    else:
        if not re.search(email_check, email):
            error_message = "Email/password format is incorrect."

        elif len(email) > 30:
            error_message = "Email/password format is incorrect."



        else:
            error_message = ""
    return error_message


'''
Validate user's password (login)
'''


def validate_login_password(password, error_message):
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
    password_check = re.compile(password_regex)

    if len(password) <= 1:
        error_message = "Email and/or password cannot be empty."

    elif len(password) < 6:
        error_message = "Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character."
    else:
        if not re.search(password_check, password):
            error_message = "Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character."
        else:
            error_message = ""
    return error_message


'''
Validate username complexity and possible username format error
# User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.
'''


def validate_username(name, error_message):
    invalidChars = set(string.punctuation.replace("_", ""))

    if len(name) <= 1:
        error_message = "User name has to be non-empty."

    else:
        if name.isdigit():
            error_message = "User name has to be alphanumeric-only."
        elif name[0] == " " or name[-1] == " ":
            error_message = "Space allowed only if it is not the first or the last character."
        elif len(name) <= 2 or len(name) >= 20:
            error_message = "User name has to be longer than 2 characters and less than 20 characters."
        elif any(x in invalidChars for x in name):
            error_message = "Incorrect Name format!"
        else:
            error_message = ""
    return error_message


'''

Validate the following:
1. Check if name of the ticket is alphanumeric-only and space is not allwed as the first or last character
2. Check if the name of the ticket is not longer than 60 chars.
3. Check if the name of the ticket contains at least 6 chars
'''


def validate_ticket_name(ticket_name, error_message):
    # count the number of alphabets in the ticket name
    count = 0
    if (ticket_name[0] == " " or ticket_name[-1] == " " or ticket_name.isalnum() == False):
        error_message = "The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character."

    if len(ticket_name) > 60:
        error_message = "The name of the ticket is no longer than 60 characters"

    for i in ticket_name:
        if (i.isalnum()):
            count += 1
    if count < 6:
        error_message = "The name of the tickets has to contain at least 6 characters"
    return error_message


# Validaet ticket quantity
def validate_ticket_quantity(ticket_quantity, error_message):
    if (ticket_quantity <= 0 or ticket_quantity > 100):
        error_message = "The quantity of the tickets has to be more than 0, and less than or equal to 100."
    return error_message


# Validate ticket price
def validate_ticket_price(ticket_price, error_message):
    if (ticket_price < 10 or ticket_price > 100):
        error_message = "Price has to be of range [10, 100]"
    return error_message


# Validate ticket date
def validate_ticket_date(ticket_date, error_message):
    expired = datetime.strptime(ticket_date, "%Y%m%d")
    present = datetime.now()

    if ticket_date != datetime.strptime(ticket_date, "%Y%m%d").strftime('%Y%m%d'):
        error_message = "Date must be given in the format YYYYMMDD (e.g. 20200901)"
    if (expired.date() < present.date()):
        error_message = "The new tickets must not be expired"
    return error_message
