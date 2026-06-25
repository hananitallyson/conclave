from utils import database
from utils import entry
from utils import interface


def crud(menu_option):
    if menu_option == 1:
        create()

        return interface.player_menu()

    elif menu_option == 2:
        find()

        return interface.player_menu()

    elif menu_option == 3:
        update()

        return interface.player_menu()

    elif menu_option == 4:
        delete()

        return interface.player_menu()

def create():
    interface.header("CREATE PLAYER")

    player_id = str(len(database.data["players"]) + 1)

    print(f"You are creating the player with ID {player_id}.\n")

    name = entry.name("NAME: ")
    email = entry.email("EMAIL: ")
    discord = entry.discord("DISCORD (e.g. @username): ")
    created_at = database.timestamp()

    database.data["players"][player_id] = {
        "name": name,
        "email": email,
        "discord": discord,
        "created_at": created_at,
        "is_deleted": False,
    }

    database.save()

    print(f"\nPlayer {player_id} created successfully!")

    interface.wait()


def find():
    interface.header("FIND PLAYER")

    player_id = entry.id("SEARCH BY PLAYER ID: ")

    if (
        player_id in database.data["players"]
        and database.data["players"][player_id]["is_deleted"] == False
    ):
        player = database.data["players"][player_id]

        interface.header("FIND PLAYER")

        interface.show_player(player)

    else:
        print("\nPlayer not found!")

    interface.wait()


def update():
    interface.header("UPDATE PLAYER")

    player_id = entry.id("SELECT THE PLAYER ID: ")
    print("")

    if (
        player_id in database.data["players"]
        and database.data["players"][player_id]["is_deleted"] == False
    ):

        player = database.data["players"][player_id]

        interface.show_player(player)

        is_confirmed = interface.confirm()

        if is_confirmed:
            interface.header("UPDATE PLAYER")

            interface.show_player(player)

            name = entry.name("NEW NAME: ")
            email = entry.email("NEW EMAIL: ")
            discord = entry.discord("NEW DISCORD: ")

            database.data["players"][player_id]["name"] = name
            database.data["players"][player_id]["email"] = email
            database.data["players"][player_id]["discord"] = discord

            database.save()

            print("\nPlayer updated successfully!")

    else:
        print("\nPlayer not found!")

    interface.wait()


def delete():
    interface.header("DELETE PLAYER")

    player_id = entry.id("SELECT THE PLAYER ID: ")

    if (
        player_id in database.data["players"]
        and database.data["players"][player_id]["is_deleted"] == False
    ):

        player = database.data["players"][player_id]

        interface.show_player(player)

        is_confirmed = interface.confirm()

        if is_confirmed:
            database.data["players"][player_id]["is_deleted"] = True

            database.save()

            print("\nPlayer deleted successfully!")

    else:
        print("\nPlayer not found!")

    interface.wait()
