from utils import database
from utils import entry
from utils import interface


def run(menu_option):
    if menu_option == 1:
        create()

        return interface.gm_menu()

    elif menu_option == 2:
        find()

        return interface.gm_menu()

    elif menu_option == 3:
        update()

        return interface.gm_menu()

    elif menu_option == 4:
        delete()

        return interface.gm_menu()


def create():
    interface.header("CREATE GAMEMASTER")

    gm_id = str(len(database.data["gamemasters"]) + 1)

    print(f"You are creating the gamemaster with ID {gm_id}.\n")

    name = entry.name("NAME: ")
    email = entry.email("EMAIL: ")
    years_experience = entry.years_experience("YEARS OF EXPERIENCE (e.g. 2): ")
    created_at = database.timestamp()

    database.data["gamemasters"][gm_id] = {
        "name": name,
        "email": email,
        "years_experience": years_experience,
        "created_at": created_at,
        "is_deleted": False,
    }

    database.save()

    print("\nGamemaster created successfully!")

    interface.wait()


def find():
    interface.header("FIND GAMEMASTER")

    gm_id = entry.id("SEARCH BY GAMEMASTER ID: ")

    if (
        gm_id in database.data["gamemasters"]
        and database.data["gamemasters"][gm_id]["is_deleted"] == False
    ):
        gm = database.data["gamemasters"][gm_id]

        interface.header("FIND GAMEMASTER")

        interface.show_gamemaster(gm)

    else:
        print("\nGamemaster not found!")

    interface.wait()


def update():
    interface.header("UPDATE GAMEMASTER")

    gm_id = entry.id("SELECT THE GAMEMASTER ID: ")

    if (
        gm_id in database.data["gamemasters"]
        and database.data["gamemasters"][gm_id]["is_deleted"] == False
    ):

        gm = database.data["gamemasters"][gm_id]

        interface.show_gamemaster(gm)

        is_confirmed = interface.confirm()

        if is_confirmed:
            interface.header("UPDATE GAMEMASTER")

            interface.show_gamemaster(gm)

            name = entry.name("NAME: ")
            email = entry.email("EMAIL: ")
            years_experience = entry.years_experience("YEARS OF EXPERIENCE: ")

            database.data["gamemasters"][gm_id]["name"] = name
            database.data["gamemasters"][gm_id]["email"] = email
            database.data["gamemasters"][gm_id]["years_experience"] = years_experience

            database.save()

            print("\nGamemaster updated successfully!")

    else:
        print("\nGamemaster not found!")

    interface.wait()


def delete():
    interface.header("DELETE GAMEMASTER")

    gm_id = entry.id("SELECT THE GAMEMASTER ID: ")

    if (
        gm_id in database.data["gamemasters"]
        and database.data["gamemasters"][gm_id]["is_deleted"] == False
    ):

        gm = database.data["gamemasters"][gm_id]

        interface.show_gamemaster(gm)

        is_confirmed = interface.confirm()

        if is_confirmed:
            database.data["gamemasters"][gm_id]["is_deleted"] = True

            database.save()

            print("\nGamemaster deleted successfully!")

    else:
        print("\nGamemaster not found!")

    interface.wait()
