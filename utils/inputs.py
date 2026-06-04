from . import validation

def name(msg):
    name = input(msg)

    while not validation.name(name):
        print("Invalid name.\nTry again!\n")
        name = input(msg)

    return name


def email(msg):
    email = input(msg)

    while not validation.email(email):
        print("Invalid email.\nTry again!\n")
        email = input(msg)

    return email


def discord(msg):
    username = input(msg)

    while not validation.username(username):
        print("Invalid discord username.\nTry again!\n")
        username = input(msg)

    return username
