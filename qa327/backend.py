from qa327.models import db, User, TicketInfo
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all backend logic that interacts with database and other services
"""
def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    # create a new user, set the balance to 5000
    new_user = User(email=email, name=name, password=hashed_pw, balance=5000, tickets=None)

    db.session.add(new_user)
    db.session.commit()
    return None

def get_ticket(name):
    """
    Get a ticket by a given name
    :param name: name of the ticket
    :return: ticket with user name
    """
    
    ticket = TicketInfo.query.filter_by(name = name).first().ticket
    return ticket


def get_all_tickets():
    """
    Get all ticket available in the database
    :param: none
    :return: list of all tickets
    """

    all_tickets = TicketInfo.query.all()
    return all_tickets


def sell_ticket(user, name, quantity, price, date):
    """
    sell the ticket in the database
    :param user: user information
    :param name: the name of the ticket
    :param quantity: the quantity of the ticket
    :param price: the price of the ticket
    :param date: the date for ticket
    :return: an error message if there is any, or None if register_ticket succeeds
    """

    ticket = TicketInfo(email=user.email, name=name, quantity=quantity, price=price, date=date)

    db.session.add(ticket)
    db.session.commit()

    return None

def get_update(name):
    """
    Check if the ticket exists in the database
    :param name: the name of the ticket
    :return: the name if ticket exists
    """
    # if this doesn't return ticket name, then the name doesn't exist
    user = get_ticket(name)
    if not user:
        return None
    return user
