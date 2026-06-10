import utils.database as database
import utils.helpers as helpers
import utils.inputs as inputs
import utils.interfaces as interfaces
from datetime import datetime

if __name__ == "__main__":
    option = ""

    interfaces.welcome()

    while option != 0:
        option = interfaces.main_menu()

        # PLAYERS
        if option == 1:
            menu_option = interfaces.player_menu()

            # CREATE PLAYER
            if menu_option == 1:
                helpers.clear()

                print("---------- CREATE PLAYER ----------")

                player_id = str(len(database.data["players"]) + 1)

                print(f"You are creating the player with ID {player_id}.\n")

                name = inputs.name("NAME: ")
                email = inputs.email("EMAIL: ")
                discord = inputs.discord("DISCORD (e.g. @username): ")
                created_at = datetime.now().isoformat()

                database.data["players"][player_id] = {
                    "name": name,
                    "email": email,
                    "discord": discord,
                    "created_at": created_at,
                }

                database.save()

                print(f"\nPlayer {player_id} created successfully!")

                interfaces.wait()

            # FIND PLAYER
            elif menu_option == 2:
                helpers.clear()

                print("---------- FIND PLAYER ----------")

                player_id = input("SEARCH BY PLAYER ID: ")

                if player_id in database.data["players"]:
                    player = database.data["players"][player_id]

                    helpers.clear()

                    print("---------- FIND PLAYER ----------")

                    print(f"ID: {player_id}")
                    print(f"NAME: {player['name']}")
                    print(f"EMAIL: {player['email']}")
                    print(f"DISCORD: {player['discord']}")

                else:
                    print("\nPlayer not found!")

                interfaces.wait()

            # UPDATE PLAYER
            elif menu_option == 3:
                helpers.clear()

                print("---------- UPDATE PLAYER ----------")

                player_id = input("SELECT THE PLAYER ID: ")

                if player_id in database.data["players"]:
                    print(f"\nYOU CHOOSE {database.data['players'][player_id]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if (yes == "Y") or (yes == ""):
                        helpers.clear()

                        print("---------- UPDATE PLAYER ----------")

                        name = inputs.name("NAME: ")
                        email = inputs.email("EMAIL: ")
                        discord = inputs.discord("DISCORD: ")

                        database.data["players"][player_id]["name"] = name
                        database.data["players"][player_id]["email"] = email
                        database.data["players"][player_id]["discord"] = discord

                        database.save()

                        print("\nPlayer updated successfully!")

                else:
                    print("\nPlayer not found!")

                interfaces.wait()

            # DELETE PLAYER
            elif menu_option == 4:
                helpers.clear()

                print("---------- DELETE PLAYER ----------")

                player_id = inputs.id("SELECT THE PLAYER ID: ")

                if player_id in database.data["players"]:
                    print(f"\nYOU CHOOSE {database.data['players'][player_id]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if (yes == "Y") or (yes == ""):
                        del database.data["players"][player_id]

                        database.save()

                        print("\nPlayer deleted successfully!")

                else:
                    print("\nPlayer not found!")

                interfaces.wait()

        # GAMEMASTERS
        elif option == 2:
            menu_option = interfaces.gm_menu()

            # CREATE GAMEMASTER
            if menu_option == 1:
                helpers.clear()

                print("---------- CREATE GAMEMASTER ----------")

                gm_id = str(len(database.data["gamemasters"]) + 1)

                print(f"You are creating the gamemaster with ID {gm_id}.\n")

                name = inputs.name("NAME: ")
                email = inputs.email("EMAIL: ")
                years_experience = inputs.years_experience(
                    "YEARS OF EXPERIENCE (e.g. 2): "
                )
                created_at = datetime.now().isoformat()

                database.data["gamemasters"][gm_id] = {
                    "name": name,
                    "email": email,
                    "years_experience": years_experience,
                    "created_at": created_at,
                }

                database.save()

                print("\nGamemaster created successfully!")

                interfaces.wait()

            # FIND GAMEMASTER
            elif menu_option == 2:
                helpers.clear()

                print("---------- FIND GAMEMASTER ----------")

                gm_id = inputs.id("SEARCH BY GAMEMASTER ID: ")

                if gm_id in database.data["gamemasters"]:
                    gm = database.data["gamemasters"][gm_id]

                    helpers.clear()

                    print("---------- FIND GAMEMASTER ----------")

                    print(f"ID: {gm_id}")
                    print(f"NAME: {gm['name']}")
                    print(f"EMAIL: {gm['email']}")
                    print(f"YEARS OF EXPERIENCE: {gm['years_experience']}")

                else:
                    print("\nGamemaster not found!")

                interfaces.wait()

            # UPDATE GAMEMASTER
            elif menu_option == 3:
                helpers.clear()

                print("---------- UPDATE GAMEMASTER ----------")

                gm_id = inputs.id("SELECT THE GAMEMASTER ID: ")

                if gm_id in database.data["gamemasters"]:
                    print(f"\nYOU CHOOSE {database.data['gamemasters'][gm_id]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if (yes == "Y") or (yes == ""):
                        helpers.clear()

                        print("---------- UPDATE GAMEMASTER ----------")

                        name = inputs.name("NAME: ")
                        email = inputs.email("EMAIL: ")
                        years_experience = inputs.years_experience(
                            "YEARS OF EXPERIENCE: "
                        )

                        database.data["gamemasters"][gm_id]["name"] = name
                        database.data["gamemasters"][gm_id]["email"] = email
                        database.data["gamemasters"][gm_id][
                            "years_experience"
                        ] = years_experience

                        database.save()

                        print("\nGamemaster updated successfully!")

                else:
                    print("\nGamemaster not found!")

                interfaces.wait()

            # DELETE GAMEMASTER
            elif menu_option == 4:
                helpers.clear()

                print("---------- DELETE GAMEMASTER ----------")

                gm_id = inputs.id("SELECT THE GAMEMASTER ID: ")

                if gm_id in database.data["gamemasters"]:
                    print(f"\nYOU CHOOSE {database.data['gamemasters'][gm_id]['name']}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if (yes == "Y") or (yes == ""):
                        del database.data["gamemasters"][gm_id]

                        database.save()

                        print("\nGamemaster deleted successfully!")

                else:
                    print("\nGamemaster not found!")

                interfaces.wait()

        # PARTIES
        elif option == 3:
            menu_option = interfaces.party_menu()

            # CREATE PARTY
            if menu_option == 1:
                helpers.clear()

                print("---------- CREATE PARTY ----------")

                party_id = str(len(database.data["parties"]) + 1)

                print(f"You are creating the party with ID {party_id}.\n")

                gamemaster_id = inputs.id("GAMEMASTER ID: ")

                if gamemaster_id not in database.data["gamemasters"]:
                    print("\nGamemaster not found!")

                    interfaces.wait()
                else:
                    players = input("PLAYERS IDs (e.g. 1 3 5): ").split(" ")

                    game = input("GAMERULES: ")

                    created_at = datetime.now().isoformat()

                    database.data["parties"][party_id] = {
                        "gamemaster_id": gamemaster_id,
                        "number_of_players": len(players),
                        "player_ids": players,
                        "game": game,
                        "created_at": created_at,
                    }

                    database.save()

                    print("\nParty created successfully!")

                    interfaces.wait()

            # FIND PARTY
            elif menu_option == 2:
                helpers.clear()

                print("---------- FIND PARTY ----------")

                party_id = inputs.id("SEARCH BY PARTY ID: ")

                if party_id in database.data["parties"]:
                    party = database.data["parties"][party_id]

                    helpers.clear()

                    print("---------- FIND PARTY ----------")

                    print(f"ID: {party_id}")
                    print(
                        f"GAMEMASTER: {database.data['gamemasters'][party['gamemaster_id']]['name']}"
                    )
                    print(f"GAME: {party['game']}")
                    print(f"NUMBER OF PLAYERS: {party['number_of_players']}")
                    print("PLAYERS:")
                    for player_id in party["player_ids"]:
                        player = database.data["players"][player_id]
                        print(f"- {player['name']} ({player['discord']})")

                else:
                    print("\nParty not found!")

                interfaces.wait()

            # UPDATE PARTY
            elif menu_option == 3:
                helpers.clear()

                print("---------- UPDATE PARTY ----------")

                party_id = inputs.id("SELECT THE PARTY ID: ")

                created_at = database.data["parties"][party_id]["created_at"]

                if party_id in database.data["parties"]:
                    print(f"\nYOU CHOOSE PARTY {party_id}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if (yes == "Y") or (yes == ""):
                        gamemaster_id = input("NEW GAMEMASTER ID: ")

                        if gamemaster_id not in database.data["gamemasters"]:
                            print("\nGamemaster not found!")

                            interfaces.wait()

                            continue

                        players = input("NEW PLAYERS IDs (e.g. 1 3 5): ").split(" ")

                        game = input("NEW GAMERULES: ")

                        database.data["parties"][party_id] = {
                            "gamemaster": gamemaster_id,
                            "number_of_players": len(players),
                            "players": players,
                            "game": game,
                            "created_at": created_at,
                        }

                        database.save()

                        print("\nParty updated successfully!")

                else:
                    print("\nParty not found!")

                interfaces.wait()

            # DELETE PARTY
            elif menu_option == 4:
                helpers.clear()

                print("---------- DELETE PARTY ----------")

                party_id = inputs.id("SELECT THE PARTY ID: ")

                if party_id in database.data["parties"]:
                    print(f"\nYOU CHOOSE PARTY {party_id}")

                    yes = input("CONTINUE? (Y/N): ").upper()

                    if (yes == "Y") or (yes == ""):
                        del database.data["parties"][party_id]

                        database.save()

                        print("\nParty deleted successfully!")

                else:
                    print("\nParty not found!")

                interfaces.wait()

        # LOGS
        elif option == 4:
            menu_option = interfaces.log_menu()

            if menu_option != 0:
                interfaces.todo()

        elif option == 0:
            print("\nExiting...\n")

