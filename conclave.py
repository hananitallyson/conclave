import subprocess
import json
import utils.validation as validation
from datetime import datetime

with open("database.json", "r", encoding="utf-8") as db:
    database = json.load(db)


def clear():
    subprocess.run("clear")


def save_database():
    with open("db.json", "w", encoding="utf-8") as db:
        json.dump(database, db, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    option = ""

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

                name = input_name("NAME: ")
                email = input_email("EMAIL: ")
                discord = input_discord("DISCORD (e.g. @username): ")
                created_at = datetime.now().isoformat()

                database["players"][player_id] = {
                    "name": name,
                    "email": email,
                    "discord": discord,
                    "created_at": created_at,
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
                    print(f"DISCORD: {player['discord']}")

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

                    if (yes == "Y") or (yes == ""):
                        clear()

                        print("---------- UPDATE PLAYER ----------")

                        name = input("NAME: ")
                        email = input("EMAIL: ")
                        discord = input("DISCORD: ")

                        database["players"][player_id]["name"] = name
                        database["players"][player_id]["email"] = email
                        database["players"][player_id]["discord"] = discord

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

                    if (yes == "Y") or (yes == ""):
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
                years_experience = int(input("YEARS OF EXPERIENCE (e.g. 2): "))
                created_at = datetime.now().isoformat()

                database["gamemasters"][gm_id] = {
                    "name": name,
                    "email": email,
                    "years_experience": years_experience,
                    "created_at": created_at
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
                    print(f"YEARS OF EXPERIENCE: {gm['years_experience']}")

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

                    if (yes == "Y") or (yes == ""):
                        clear()

                        print("---------- UPDATE GAMEMASTER ----------")

                        name = input("NAME: ")
                        email = input("EMAIL: ")
                        years_experience = input("YEARS OF EXPERIENCE: ")

                        database["gamemasters"][gm_id]["name"] = name
                        database["gamemasters"][gm_id]["email"] = email
                        database["gamemasters"][gm_id]["years_experience"] = years_experience

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

                    if (yes == "Y") or (yes == ""):
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

                    created_at = datetime.now().isoformat()

                    database["parties"][party_id] = {
                        "gamemaster_id": gamemaster_id,
                        "number_of_players": len(players),
                        "player_ids": players,
                        "game": game,
                        "created_at": created_at
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
                    print(f"GAMEMASTER: {database['gamemasters'][party['gamemaster_id']]['name']}")
                    print(f"GAME: {party['game']}")
                    print(f"NUMBER OF PLAYERS: {party['number_of_players']}")
                    print("PLAYERS:")
                    for player_id in party["player_ids"]:
                        player = database["players"][player_id]
                        print(f"- {player['name']} ({player['discord']})")

                else:
                    print("\nParty not found!")

                input("\nPress ENTER to continue...")

            # UPDATE PARTY
            elif menu_option == 3:
                clear()

                print("---------- UPDATE PARTY ----------")

                party_id = input("SELECT THE PARTY ID: ")

                created_at = database["parties"][party_id]["created_at"]

                if party_id in database["parties"]:
                    print(f"\nYOU CHOOSE PARTY {party_id}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if (yes == "Y") or (yes == ""):
                        gamemaster_id = input("NEW GAMEMASTER ID: ")

                        if gamemaster_id not in database["gamemasters"]:
                            print("\nGamemaster not found!")

                            input("\nPress ENTER to continue...")

                            continue

                        players = input("NEW PLAYERS IDs (e.g. 1 3 5): ").split(" ")

                        game = input("NEW GAMERULES: ")

                        database["parties"][party_id] = {
                            "gamemaster": gamemaster_id,
                            "number_of_players": len(players),
                            "players": players,
                            "game": game,
                            "created_at": created_at
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

                    if (yes == "Y") or (yes == ""):
                        del database["parties"][party_id]

                        save_database()

                        print("\nParty deleted successfully!")

                else:
                    print("\nParty not found!")

                input("\nPress ENTER to continue...")

        # LOGS
        elif option == 4:
            menu_option = log_menu()

            if menu_option != 0:
                todo()

        elif option == 0:
            print("\nExiting...\n")

