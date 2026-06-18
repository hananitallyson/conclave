# Only letters and spaces,
# and 2 to 100 characters.
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

            if local and "." in domain:
                is_valid = True

    return is_valid


# Starts with @, 2-32 letters, numbers or _.
def username(username):
    is_valid = False
    username = username.strip()

    if username.startswith("@"):
        handle = username[1:]

        if 2 <= len(handle) <= 32 and handle.replace("_", "").isalnum():
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
