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


def years_experience(msg):
    years = input(msg)

    while not validation.years_experience(years):
          print("Invalid number of years.\nTry again!\n")
          years = input(msg)

    return int(years)
