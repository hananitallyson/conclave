def name(name):
    is_valid = False
    name = name.strip()

    if name and len(name) >= 2:
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
