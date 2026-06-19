from . import validate

def name(msg):
    name = input(msg)

    while not validate.name(name):
        print("Invalid name.\nTry again!\n")
        name = input(msg)

    return name


def email(msg):
    email = input(msg)

    while not validate.email(email):
        print("Invalid email.\nTry again!\n")
        email = input(msg)

    return email


def discord(msg):
    username = input(msg)

    while not validate.username(username):
        print("Invalid discord username.\nTry again!\n")
        username = input(msg)

    return username


def years_experience(msg):
    years = input(msg)

    while not validate.years_experience(years):
          print("Invalid number of years.\nTry again!\n")
          years = input(msg)

    return int(years)

def id(msg):
    id = input(msg)

    while not validate.id(id):
        print("Invalid id.\nTry again!\n")
        id = input(msg)

    return id

def game(msg):
    game = input(msg)

    while not validate.game(game):
        print("Invalid gamerule name.\nTry again!\n")
        game = input(msg)


    return game

def players(msg):
    players = input(msg)

    while not validate.players([int(id) for id in players]):
        print("Invalid players id.\nTry again!\n")
        players = input(msg)


    return players


def date(msg):
    date = input(msg)

    while not validate.date(date):
        print("Invalid date time.\nTry again!\n")
        date = input(msg)

    return date
