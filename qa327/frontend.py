from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn
import re #regular expressions
import string

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
# If the email already exists, show message 'this email has been ALREADY used'

'''
def validate_email(email, error_message, user):
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if len(email) <= 1:
        error_message = "Email and/or password cannot be empty."

    else :
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
        if (not re.search(password_check, password)) and  password == password2:
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
    if len(email) <= 1:
        error_message = "Email and/or password cannot be empty."

    else :
        if not re.search(email_regex, email):
            error_message = "Email/password format is incorrect."
        
        elif len(email) > 30:
            error_message = "Email/password format is incorrect."
            
        elif user:
            session['logged_in'] = user.email
            return redirect('/', code=303)
            
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
    #email
    if check_pwd == "" and check_name == "":
        if check_email != "":
            return render_template('register.html', message=check_email)
            
    if check_pwd == "" or check_name == "":
        if check_email != "":
            return render_template('register.html', message=check_email)

    #password
    if check_email == "" and check_name == "":
        if check_pwd != "":
            return render_template('register.html', message=check_pwd)
    
    #name
    if check_email == "" and check_pwd == "":
        if check_name != "":
            return render_template('register.html', message=check_name)
    
    #fail to store
    if not bn.register_user(email, name, password, password2):
            error_message = "Failed to store user info."

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
    error_message = None
    
    # validate email
    check_email = validate_login_email(email, error_message, user)
    
    # validate password and password2
    check_pwd = validate_login_password(password, error_message)
    
    # For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
    #email
    if check_pwd == "":
        if check_email != "":
            return render_template('login.html', message=check_email)
    #password
    if check_email == "":
        if check_pwd != "":
            return render_template('login.html', message=check_pwd)
    
    if check_pwd != "" and check_pwd != "":
        if check_pwd == check_email:
            return render_template('login.html', message=check_email)
        
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
