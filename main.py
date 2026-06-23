import utils.database as database
import utils.entry as entry
import utils.helper as helper
import utils.interface as interface

if __name__ == "__main__":
    option = ""

    interface.welcome()

    while option != 0:
        option = interface.main_menu()

        # PLAYERS
        if option == 1:
            menu_option = interface.player_menu()
            while menu_option != 0:
                # CREATE PLAYER
                if menu_option == 1:
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

                    menu_option = interface.player_menu()

                # FIND PLAYER
                elif menu_option == 2:
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

                    menu_option = interface.player_menu()

                # UPDATE PLAYER
                elif menu_option == 3:
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

                    menu_option = interface.player_menu()

                # DELETE PLAYER
                elif menu_option == 4:
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

                    menu_option = interface.player_menu()

        # GAMEMASTERS
        elif option == 2:
            menu_option = interface.gm_menu()
            while menu_option != 0:
                # CREATE GAMEMASTER
                if menu_option == 1:
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

                    menu_option = interface.gm_menu()

                # FIND GAMEMASTER
                elif menu_option == 2:
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

                    menu_option = interface.gm_menu()

                # UPDATE GAMEMASTER
                elif menu_option == 3:
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

                    menu_option = interface.gm_menu()

                # DELETE GAMEMASTER
                elif menu_option == 4:
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

                    menu_option = interface.gm_menu()

        # PARTIES
        elif option == 3:
            menu_option = interface.party_menu()
            while menu_option != 0:
                # CREATE PARTY
                if menu_option == 1:
                    interface.header("CREATE PARTY")

                    party_id = str(len(database.data["parties"]) + 1)

                    print(f"You are creating the party with ID {party_id}.\n")

                    gamemaster_id = entry.id("GAMEMASTER ID: ")

                    if gamemaster_id not in database.data["gamemasters"]:
                        print("\nGamemaster not found!")

                        interface.wait()
                    else:
                        players = input("PLAYERS IDs (e.g. 1 3 5): ").split(" ")

                        game = input("GAMERULES: ")

                        created_at = database.timestamp()

                        database.data["parties"][party_id] = {
                            "gamemaster_id": gamemaster_id,
                            "number_of_players": len(players),
                            "player_ids": players,
                            "game": game,
                            "created_at": created_at,
                            "is_deleted": False,
                        }

                        database.save()

                        print("\nParty created successfully!")

                        interface.wait()

                        menu_option = interface.party_menu()

                # FIND PARTY
                elif menu_option == 2:
                    interface.header("FIND PARTY")

                    party_id = entry.id("SEARCH BY PARTY ID: ")

                    if (
                        party_id in database.data["parties"]
                        and database.data["parties"][party_id]["is_deleted"] == False
                    ):
                        party = database.data["parties"][party_id]

                        interface.header("FIND PARTY")

                        if database.data["gamemasters"][party["gamemaster_id"]]["is_deleted"] == False:
                            print(f"GAMEMASTER: {database.data['gamemasters'][party['gamemaster_id']]['name']}")
                        else:
                            print(
                                f"GAMEMASTER: {database.data['gamemasters'][party['gamemaster_id']]['name']} <deleted>"
                            )
                        print(f"GAME: {party['game']}")
                        print(f"NUMBER OF PLAYERS: {party['number_of_players']}")
                        print("PLAYERS:")
                        for player_id in party["player_ids"]:
                            player = database.data["players"][player_id]
                            if player["is_deleted"] == False:
                                print(f"- {player['name']} ({player['discord']})")
                            else:
                                print(f"- {player['name']} ({player['discord']}) <deleted>")

                    else:
                        print("\nParty not found!")

                    interface.wait()

                    menu_option = interface.party_menu()

                # UPDATE PARTY
                elif menu_option == 3:
                    interface.header("UPDATE PARTY")

                    party_id = entry.id("SELECT THE PARTY ID: ")

                    if (
                        party_id in database.data["parties"]
                        and database.data["parties"][party_id]["is_deleted"] == False
                    ):
                        print(f"\nYOU CHOOSE PARTY {party_id}")

                        is_confirmed = interface.confirm()

                        if is_confirmed:
                            created_at = database.data["parties"][party_id]["created_at"]
                            gamemaster_id = entry.id("\nNEW GAMEMASTER ID: ")

                            if gamemaster_id not in database.data["gamemasters"]:
                                print("\nGamemaster not found!")

                                interface.wait()

                                continue

                            players = input("NEW PLAYERS IDs (e.g. 1 3 5): ").split(" ")

                            game = entry.game("NEW GAMERULES: ")

                            database.data["parties"][party_id] = {
                                "gamemaster_id": gamemaster_id,
                                "number_of_players": len(players),
                                "player_ids": players,
                                "game": game,
                                "created_at": created_at,
                                "is_deleted": False,
                            }

                            database.save()

                            print("\nParty updated successfully!")

                    else:
                        print("\nParty not found!")

                    interface.wait()

                    menu_option = interface.party_menu()

                # DELETE PARTY
                elif menu_option == 4:
                    interface.header("DELETE PARTY")

                    party_id = entry.id("SELECT THE PARTY ID: ")

                    if (
                        party_id in database.data["parties"]
                        and database.data["parties"][party_id]["is_deleted"] == False
                    ):
                        print(f"\nYOU CHOOSE PARTY {party_id}")

                        is_confirmed = interface.confirm()

                        if is_confirmed:
                            database.data["parties"][party_id]["is_deleted"] = True

                            database.save()

                            print("\nParty deleted successfully!")

                    else:
                        print("\nParty not found!")

                    interface.wait()

                    menu_option = interface.party_menu()

        # LOGS
        elif option == 4:
            menu_option = interface.log_menu()
            while menu_option != 0:
                # LIST PLAYERS
                if menu_option == 1:
                    interface.header("CONCLAVE PLAYERS")
                    print(f"{'ID':<8} {'PLAYER':<20} {'EMAIL':<30} {'DISCORD':<20}")
                    print("=" * 85)

                    for player_id, player in database.data["players"].items():
                        if player["is_deleted"] == False:
                            print(
                                f"{player_id:<8} "
                                f"{player['name']:<20} "
                                f"{player['email']:<30} "
                                f"{player['discord']:<20}"
                            )

                    print("=" * 85)

                    interface.wait()

                    menu_option = interface.log_menu()

                # LIST GAMEMASTERS
                elif menu_option == 2:
                    interface.header("CONCLAVE GAMEMASTERS")
                    print(f"{'ID':<8} {'GAMEMASTER':<20} {'EMAIL':<30} {'EXPERIENCE':<20}")
                    print("=" * 85)

                    for gamemaster_id, gamemaster in database.data["gamemasters"].items():
                        if gamemaster["is_deleted"] == False:
                            experience = f"{gamemaster['years_experience']} yrs"
                            print(
                                f"{gamemaster_id:<8} "
                                f"{gamemaster['name']:<20} "
                                f"{gamemaster['email']:<30} "
                                f"{experience:<20}"
                            )

                    print("=" * 85)

                    interface.wait()

                    menu_option = interface.log_menu()

                # LIST PARTIES BY GAME
                elif menu_option == 3:
                    interface.header("CONCLAVE PARTIES BY GAME")
                    game_chosen = entry.game("ENTER A GAME: ")

                    if game_chosen in [party["game"] for party in database.data["parties"].values()]:
                        print(f"\n{'PARTY ID':<12} {'GAMEMASTER':<20} {'NUMBER OF PLAYERS':<30} {'PLAYERS':<20}")
                        print("=" * 98)

                        for party_id, party in database.data["parties"].items():
                            if game_chosen == party["game"] and party["is_deleted"] == False:
                                players = ", ".join(
                                    database.data["players"][player_id]["name"] for player_id in party["player_ids"]
                                )

                                print(
                                    f"{party_id:<12} "
                                    f"{database.data['gamemasters'][party['gamemaster_id']]['name']:<20} "
                                    f"{party['number_of_players']:<30} "
                                    f"{players:<20}"
                                )

                        print("=" * 98)
                    else:
                        print("\nThe game is not present in the database.")

                    interface.wait()

                    menu_option = interface.log_menu()

                # LIST PLAYERS & GAMEMASTERS BY DATE
                elif menu_option == 4:
                    interface.header("CONCLAVE PLAYERS & GAMEMASTERS BY DATE")
                    date_filter = helper.fromiso(entry.date("CREATED FROM (YYYY-MM-DD): "))

                    print(f"\n{'ID':<8} {'TYPE':<12} {'NAME':<20} {'CREATED AT':<20}")
                    print("=" * 65)

                    for player_id, player in database.data["players"].items():
                        if helper.fromiso(player["created_at"]) >= date_filter:
                            if player["is_deleted"] == False:
                                print(
                                    f"{player_id:<8} "
                                    f"{'Player':<12} "
                                    f"{player['name']:<20} "
                                    f"{helper.timestring(player['created_at'])[:19]:<20}"
                                )

                    print("-" * 65)

                    for gm_id, gamemaster in database.data["gamemasters"].items():
                        if helper.fromiso(gamemaster["created_at"]) >= date_filter:
                            if gamemaster["is_deleted"] == False:
                                print(
                                    f"{gm_id:<8} "
                                    f"{'Gamemaster':<12} "
                                    f"{gamemaster['name']:<20} "
                                    f"{helper.timestring(gamemaster['created_at'])[:19]:<20}"
                                )

                    print("=" * 65)

                    interface.wait()

                    menu_option = interface.log_menu()

                # LIST PLAYERS BY GAMEMASTERS
                elif menu_option == 5:
                    interface.header("CONCLAVE PLAYERS BY GAMEMASTER")

                    gm_id = entry.id("ENTER GAMEMASTER ID: ")

                    if gm_id not in database.data["gamemasters"]:
                        print("\nGamemaster not found!")
                    else:
                        gm = database.data["gamemasters"][gm_id]

                        if gm["is_deleted"] == False:
                            print(f"\nGAMEMASTER: {gm['name']}\n")
                        else:
                            print(f"\nGAMEMASTER: {gm['name']} <deleted>\n")

                        print(f"{'PLAYER':<20} {'PARTY ID':<10}")
                        print("=" * 35)

                        found = False
                        player_parties = {}
                        for party_id, party in database.data["parties"].items():
                            if party["gamemaster_id"] == gm_id:
                                found = True
                                for player_id in party["player_ids"]:
                                    if player_id not in player_parties:
                                        player_parties[player_id] = []
                                    player_parties[player_id].append(party_id)

                        for player_id, party_ids in player_parties.items():
                            name = database.data["players"][player_id]["name"]
                            parties_str = ", ".join(party_ids)
                            print(f"{name:<20} {parties_str}")

                        if not found:
                            print("No parties found for this gamemaster.")

                        print("=" * 35)

                    interface.wait()

                    menu_option = interface.log_menu()

        elif option == 0:
            interface.exit()

