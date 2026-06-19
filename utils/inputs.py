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

def id(msg):
    id = input(msg)

    while not validation.id(id):
        print("Invalid id.\nTry again!\n")
        id = input(msg)

    return id

def game(msg):
    game = input(msg)

    while not validation.game(game):
        print("Invalid gamerule name.\nTry again!\n")

    return game

def players(msg):
    players = input(msg)

    while not validation.players([int(id) for id in players]):
        print("Invalid players id.\nTry again!\n")

    return players


def date(msg):
    date = input(msg)

    while not validation.date(date):
        print("Invalid date time.\nTry again!\n")

    return date
