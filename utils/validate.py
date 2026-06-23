import datetime


# Only letters and spaces,
# and 2 to 100 characters.
def name(name):
    is_valid = False
    name = name.strip()

    if name and (len(name) >= 2) and (len(name) <= 100):
        words = name.split()
        all_words_valid = True

        for word in words:
            if not word.isalpha():
                all_words_valid = False

        if all_words_valid:
            is_valid = True

    return is_valid


# Must have one @, text before it,
# and a dot in the domain.
def email(email):
    is_valid = False
    email = email.strip()

    if "@" in email:
        parts = email.split("@")

        if len(parts) == 2:
            local = parts[0]
            domain = parts[1]

            if local and ("." in domain):
                is_valid = True

    return is_valid


# Starts with @, 2-32 letters, numbers or _.
def username(username):
    is_valid = False
    username = username.strip()

    if username.startswith("@"):
        handle = username[1:]

        if (2 <= len(handle) <= 32) and (handle.replace("_", "").isalnum()):
            is_valid = True

    return is_valid


# A number between 0 and 70.
def years_experience(years):
    is_valid = False
    years_int = int(years)

    if 0 <= years_int <= 70:
        is_valid = True

    return is_valid


# A positive number above zero.
def id(id):
    is_valid = False

    if id.isdigit() and (int(id) > 0):
        is_valid = True

    return is_valid


# Text between 2 and 100 characters.
def game(game):
    is_valid = False
    game = game.strip()

    if game and (2 <= len(game) <= 100):
        is_valid = True

    return is_valid


# Date YYYY-MM-DD
def date(date):
    is_valid = False
    date = date.strip()

    if (len(date) == 10) and (date[4] == "-") and (date[7] == "-"):
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]

        if year.isdigit() and month.isdigit() and day.isdigit():
            year = int(year)
            month = int(month)
            day = int(day)

            if (0 < year <= datetime.date.today().year) and (0 < month <= datetime.date.today().month) and (0 < day <= datetime.date.today().day):
                is_valid = True

    return is_valid

