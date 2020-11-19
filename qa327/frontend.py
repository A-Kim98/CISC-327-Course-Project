from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn
import re #regular expressions

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""

@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')

'''
Validate email complexity and possible email format errors
# Email, password, password2 all have to satisfy the same required as defined in R1
# Email and password both cannot be empty
# Email has to follow addr-spec defined in RFC 5322
'''
@app.route('/register', methods=['POST'])
def validate_email(mail, pwd1, pwd2):
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if len(mail) <= 1 and (len(pwd1) <= 1 or len(pwd2) <= 1):
        error_message = "Email and/or password cannot be empty."

    elif len(mail) > 2 and (len(pwd1) > 1 or len(pwd2) > 1):
        if not re.search(email_regex, mail):
            error_message = "Email/password format is incorrect."
        
        elif len(mail) > 25:
            error_message = "Email/password format is incorrect."
    else:
        error_message = ""
    return error_message

'''
Validate password complexity and possible password/password2 format error
# Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
'''
@app.route('/register', methods=['POST'])
def validate_password(pwd1, pwd2):
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
    password_check = re.compile(password_regex)
    
    if len(pwd1) < 6 or len(pwd2) < 6:
        error_message = "Password needs minimum length 6"
    
    elif len(pwd1) > 6 and len(pwd2) > 6:
        if (not re.search(password_check, pwd1)) and  pwd1 == pwd2:
            error_message = "Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character."
        elif pwd1 != pwd2:
            error_message = "Password and password2 have to be exactly the same."
        elif not re.match(r'^\w+$', pwd1):
            error_message = "Email/password format is incorrect."
        elif not re.match(r'^\w+$', pwd2):
            error_message = "Email/password format is incorrect."
    else:
        error_message = ""
    return error_message


'''
Validate username complexity and possible username format error
# User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.
'''
@app.route('/register', methods=['POST'])
def validate_username(user):
    if len(user) <= 1:
        error_message = "User name has to be non-empty."
        
    elif len(user) > 1:
        if user.isdigit():
            error_message = "User name has to be alphanumeric-only."
        elif user[0] == " " or user[-1] == " ":
            error_message = "Space allowed only if it is not the first or the last character."
        elif user(user) <= 2 or len(user) >= 20:
            error_message = "User name has to be longer than 2 characters and less than 20 characters."
        elif re.match(r'^\w+$', user):
            error_message = "Name format is incorrect."
    else:
        error_message = ""
    return error_message
    
# The registration form can be submitted as a POST request to the current URL (/register)
@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    # validate email
    check_email = validate_email(email, password, password2)
    user = bn.get_user(email)

    # validate password and password2
    check_pwd = validate_password(password, password2)
    
    # validate username
    check_name = validate_username(name)
    
    # validate user informations
    if check_pwd == "" and check_name == "":
        if check_email != "":
            return render_template('register.html', message=check_email)
    if check_email == "" and check_name == "":
        if check_pwd != "":
            return render_template('register.html', message=check_pwd)
    if check_email == "" and check_pwd == "":
        if check_name != "":
            return render_template('register.html', message=check_name)
   
    # If the email already exists, show message 'this email has been ALREADY used'
    if user:
        error_message = "this email has been ALREADY used"
        return render_template('register.html', message=error_message)
    
    if not bn.register_user(email, name, password, password2):
        error_message = "Failed to store user info."
        return render_template('register.html', message=error_message)

    #If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
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
    user = bn.login_user(email, password)
    
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
   
    # Email and password both cannot be empty
    if email == " " or password == " " :
        return render_template('login.html', message= "Email and/or password cannot be empty.")
        
    # Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
    if len(password) < 6:
        return render_template('login.html', message="Password needs minimum length 6.")
    
    # at least one upper case, at least one lower case, and at least one special character
    if len(password) > 6:
        if len(re.findall(r'[A-Z]',password)) < 1:
            return render_template('login.html', message="Password needs at least one upper case.")
        elif len(re.findall(r'[a-z]',password)) < 1:
            return render_template('login.html', message="Password needs at least one lower case.")
        elif len(re.findall(r'\b\S+\b',password)) < 1:
            return render_template('login.html', message="Password needs at least one special character.")
    
    # For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
    if not re.search(regex, email):
        return render_template('login.html', message="email/password format is incorrect.")
    
    
    # If email/password are correct, redirect to /
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
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
