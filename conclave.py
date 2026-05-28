import subprocess
import json

with open("db.json", "r", encoding="utf-8") as db:
    database = json.load(db)


def clear():
    subprocess.run("clear")


def save_database():
    with open("db.json", "w", encoding="utf-8") as db:
        json.dump(database, db, indent=4, ensure_ascii=False)


def welcome():
    clear()

    print(r"""
          _______  _        _______  _______  _______  _______ 
|\     /|(  ____ \( \      (  ____ \(  ___  )(       )(  ____ \
| )   ( || (    \/| (      | (    \/| (   ) || () () || (    \/
| | _ | || (__    | |      | |      | |   | || || || || (__    
| |( )| ||  __)   | |      | |      | |   | || |(_)| ||  __)   
| || || || (      | |      | |      | |   | || |   | || (      
| () () || (____/\| (____/\| (____/\| (___) || )   ( || (____/\
(_______)(_______/(_______/(_______/(_______)|/     \|(_______/

                 Welcome to Conclave!
""")

    input("\nPress ENTER to continue...")


def main_menu():
    clear()

    print("---------- CONCLAVE MENU ----------")
    print("(1) PLAYERS")
    print("(2) GAMEMASTERS")
    print("(3) PARTIES")
    print("(0) EXIT")

    option = input("\n *  Choose your option: ")

    match option:
        case "0":
            option = 0
        case "1":
            option = 1
        case "2":
            option = 2
        case "3":
            option = 3
        case "4":
            option = 4
        case _:
            option = 1

    return option


def player_menu():
    clear()

    print("---------- PLAYERS ----------")
    print("(1) NEW PLAYER")
    print("(2) FIND PLAYER")
    print("(3) UPDATE PLAYER")
    print("(4) DELETE PLAYER")
    print("(0) EXIT")

    option = input("\n *  Choose your option: ")

    match option:
        case "0":
            option = 0
        case "1":
            option = 1
        case "2":
            option = 2
        case "3":
            option = 3
        case "4":
            option = 4
        case _:
            option = 2

    return option


def gm_menu():
    clear()

    print("---------- GAMEMASTERS ----------")
    print("(1) NEW GAMEMASTER")
    print("(2) FIND GAMEMASTER")
    print("(3) UPDATE GAMEMASTER")
    print("(4) DELETE GAMEMASTER")
    print("(0) EXIT")

    option = input("\n *  Choose your option: ")

    match option:
        case "0":
            option = 0
        case "1":
            option = 1
        case "2":
            option = 2
        case "3":
            option = 3
        case "4":
            option = 4
        case _:
            option = 2

    return option


def party_menu():
    clear()

    print("---------- PARTIES ----------")
    print("(1) NEW PARTY")
    print("(2) FIND PARTY")
    print("(3) UPDATE PARTY")
    print("(4) DELETE PARTY")
    print("(0) EXIT")

    option = input("\n *  Choose your option: ")

    match option:
        case "0":
            option = 0
        case "1":
            option = 1
        case "2":
            option = 2
        case "3":
            option = 3
        case "4":
            option = 4
        case _:
            option = 2

    return option


if __name__ == "__main__":
    option = -1

    welcome()

    while option != 0:
        option = main_menu()

        # PLAYERS
        if option == 1:
            menu_option = player_menu()

            # CREATE PLAYER
            if menu_option == 1:
                clear()

                print("---------- CREATE PLAYER ----------")

                player_id = str(len(database["players"]) + 1)

                print(f"You are creating the player with ID {player_id}.\n")

                name = input("NAME: ")
                email = input("EMAIL: ")
                phone = input("PHONE NUMBER: ")

                database["players"][player_id] = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                }

                save_database()

                print(f"\nPlayer {player_id} created successfully!")

                input("\nPress ENTER to continue...")

            # FIND PLAYER
            elif menu_option == 2:
                clear()

                print("---------- FIND PLAYER ----------")

                player_id = input("SEARCH BY PLAYER ID: ")

                if player_id in database["players"]:
                    player = database["players"][player_id]

                    clear()

                    print("---------- FIND PLAYER ----------")

                    print(f"ID: {player_id}")
                    print(f"NAME: {player['name']}")
                    print(f"EMAIL: {player['email']}")
                    print(f"PHONE NUMBER: {player['phone']}")

                else:
                    print("\nPlayer not found!")

                input("\nPress ENTER to continue...")

            # UPDATE PLAYER
            elif menu_option == 3:
                clear()

                print("---------- UPDATE PLAYER ----------")

                player_id = input("SELECT THE PLAYER ID: ")

                if player_id in database["players"]:
                    print(f"\nYOU CHOOSE {database['players'][player_id]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if yes == "Y":
                        clear()

                        print("---------- UPDATE PLAYER ----------")

                        name = input("NAME: ")
                        email = input("EMAIL: ")
                        phone = input("PHONE NUMBER: ")

                        database["players"][player_id]["name"] = name
                        database["players"][player_id]["email"] = email
                        database["players"][player_id]["phone"] = phone

                        save_database()

                        print("\nPlayer updated successfully!")

                else:
                    print("\nPlayer not found!")

                input("\nPress ENTER to continue...")

            # DELETE PLAYER
            elif menu_option == 4:
                clear()

                print("---------- DELETE PLAYER ----------")

                player_id = input("SELECT THE PLAYER ID: ")

                if player_id in database["players"]:
                    print(f"\nYOU CHOOSE {database['players'][player_id]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if yes == "Y":
                        del database["players"][player_id]

                        save_database()

                        print("\nPlayer deleted successfully!")

                else:
                    print("\nPlayer not found!")

                input("\nPress ENTER to continue...")

        # GAMEMASTERS
        elif option == 2:
            menu_option = gm_menu()

            # CREATE GAMEMASTER
            if menu_option == 1:
                clear()

                print("---------- CREATE GAMEMASTER ----------")

                gm_id = str(len(database["gamemasters"]) + 1)

                print(f"You are creating the gamemaster with ID {gm_id}.\n")

                name = input("NAME: ")
                email = input("EMAIL: ")
                phone = input("PHONE NUMBER: ")

                database["gamemasters"][gm_id] = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                }

                save_database()

                print("\nGamemaster created successfully!")

                input("\nPress ENTER to continue...")

            # FIND GAMEMASTER
            elif menu_option == 2:
                clear()

                print("---------- FIND GAMEMASTER ----------")

                gm_id = input("SEARCH BY GAMEMASTER ID: ")

                if gm_id in database["gamemasters"]:
                    gm = database["gamemasters"][gm_id]

                    clear()

                    print("---------- FIND GAMEMASTER ----------")

                    print(f"ID: {gm_id}")
                    print(f"NAME: {gm['name']}")
                    print(f"EMAIL: {gm['email']}")
                    print(f"PHONE NUMBER: {gm['phone']}")

                else:
                    print("\nGamemaster not found!")

                input("\nPress ENTER to continue...")

            # UPDATE GAMEMASTER
            elif menu_option == 3:
                clear()

                print("---------- UPDATE GAMEMASTER ----------")

                gm_id = input("SELECT THE GAMEMASTER ID: ")

                if gm_id in database["gamemasters"]:
                    print(f"\nYOU CHOOSE {database['gamemasters'][gm_id]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if yes == "Y":
                        clear()

                        print("---------- UPDATE GAMEMASTER ----------")

                        name = input("NAME: ")
                        email = input("EMAIL: ")
                        phone = input("PHONE NUMBER: ")

                        database["gamemasters"][gm_id]["name"] = name
                        database["gamemasters"][gm_id]["email"] = email
                        database["gamemasters"][gm_id]["phone"] = phone

                        save_database()

                        print("\nGamemaster updated successfully!")

                else:
                    print("\nGamemaster not found!")

                input("\nPress ENTER to continue...")

            # DELETE GAMEMASTER
            elif menu_option == 4:
                clear()

                print("---------- DELETE GAMEMASTER ----------")

                gm_id = input("SELECT THE GAMEMASTER ID: ")

                if gm_id in database["gamemasters"]:
                    print(f"\nYOU CHOOSE {database['gamemasters'][gm_id]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if yes == "Y":
                        del database["gamemasters"][gm_id]

                        save_database()

                        print("\nGamemaster deleted successfully!")

                else:
                    print("\nGamemaster not found!")

                input("\nPress ENTER to continue...")

        # PARTIES
        elif option == 3:
            menu_option = party_menu()

            # CREATE PARTY
            if menu_option == 1:
                clear()

                print("---------- CREATE PARTY ----------")

                party_id = str(len(database["parties"]) + 1)

                print(f"You are creating the party with ID {party_id}.\n")

                gamemaster_id = input("GAMEMASTER ID: ")

                if gamemaster_id not in database["gamemasters"]:
                    print("\nGamemaster not found!")

                    input("\nPress ENTER to continue...")
                else:
                    players = input("PLAYERS IDs (e.g. 1 3 5): ").split(" ")

                    game = input("GAMERULES: ")

                    player_names = []

                    for player_id in players:
                        if player_id in database["players"]:
                            player_names.append(database["players"][player_id]["name"])

                    database["parties"][party_id] = {
                        "gamemaster": database["gamemasters"][gamemaster_id]["name"],
                        "number_of_players": len(player_names),
                        "players": player_names,
                        "game": game,
                    }

                    save_database()

                    print("\nParty created successfully!")

                    input("\nPress ENTER to continue...")

            # FIND PARTY
            elif menu_option == 2:
                clear()

                print("---------- FIND PARTY ----------")

                party_id = input("SEARCH BY PARTY ID: ")

                if party_id in database["parties"]:
                    party = database["parties"][party_id]

                    clear()

                    print("---------- FIND PARTY ----------")

                    print(f"ID: {party_id}")
                    print(f"GAMEMASTER: {party['gamemaster']}")
                    print(f"GAME: {party['game']}")
                    print(f"NUMBER OF PLAYERS: {party['number_of_players']}")

                    print("PLAYERS:")

                    for player in party["players"]:
                        print(f"- {player}")

                else:
                    print("\nParty not found!")

                input("\nPress ENTER to continue...")

            # UPDATE PARTY
            elif menu_option == 3:
                clear()

                print("---------- UPDATE PARTY ----------")

                party_id = input("SELECT THE PARTY ID: ")

                if party_id in database["parties"]:
                    print(f"\nYOU CHOOSE PARTY {party_id}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if yes == "Y":
                        gamemaster_id = input("NEW GAMEMASTER ID: ")

                        if gamemaster_id not in database["gamemasters"]:
                            print("\nGamemaster not found!")

                            input("\nPress ENTER to continue...")

                            continue

                        players = input("NEW PLAYERS IDs (e.g. 1 3 5): ").split(" ")

                        game = input("NEW GAMERULES: ")

                        player_names = []

                        for player_id in players:
                            if player_id in database["players"]:
                                player_names.append(
                                    database["players"][player_id]["name"]
                                )

                        database["parties"][party_id] = {
                            "gamemaster": database["gamemasters"][gamemaster_id][
                                "name"
                            ],
                            "number_of_players": len(player_names),
                            "players": player_names,
                            "game": game,
                        }

                        save_database()

                        print("\nParty updated successfully!")

                else:
                    print("\nParty not found!")

                input("\nPress ENTER to continue...")

            # DELETE PARTY
            elif menu_option == 4:
                clear()

                print("---------- DELETE PARTY ----------")

                party_id = input("SELECT THE PARTY ID: ")

                if party_id in database["parties"]:
                    print(f"\nYOU CHOOSE PARTY {party_id}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if yes == "Y":
                        del database["parties"][party_id]

                        save_database()

                        print("\nParty deleted successfully!")

                else:
                    print("\nParty not found!")

                input("\nPress ENTER to continue...")

        elif option == 0:
            print("\nExiting...\n")

