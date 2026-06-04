def name(name):
    is_valid = False

    if name:
        is_valid = True
    else:
        is_valid = False

    return is_valid

def email(email):
    is_valid = False

    if "@" in email:
        is_valid = True
    else:
        is_valid = False

    return is_valid
