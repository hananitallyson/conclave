# Limit of 100 characters and only letters (no numbers or symbols)
def name(name):
    is_valid = False
    name = name.strip()

    if name and len(name) >= 2 and len(name) <= 100:
        words = name.split()
        all_words_valid = True

        for word in words:
            if not word.isalpha():
                all_words_valid = False

        if all_words_valid:
            is_valid = True

    return is_valid


def email(email):
    is_valid = False
    email = email.strip()

    if "@" in email and "." in email:
        is_valid = True

    return is_valid


def username(username):
    is_valid = False
    username = username.strip()

    if 2 <= len(username) <= 32 and username.startswith("@"):
        is_valid = True

    return is_valid


def years_experience(years):
    is_valid = False

    if years.isdigit():
        is_valid = True

    return is_valid


def id(id):
    is_valid = False

    if id.isdigit():
        is_valid = True

    return is_valid


def game(game):
    is_valid = False
    game = game.strip()

    if game and len(game) >= 2:
        is_valid = True

    return is_valid
