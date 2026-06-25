import utils.database as database
import utils.entry as entry
import utils.helper as helper
import utils.interface as interface
import utils.player as PlayerController
import utils.gamemaster as GamemasterController
import utils.party as PartyController

if __name__ == "__main__":
    option = ""

    interface.welcome()

    while option != 0:
        option = interface.main_menu()

        if option == 1:
            menu_option = interface.player_menu()

            while menu_option != 0:
                if menu_option == 1:
                    PlayerController.create()

                    menu_option = interface.player_menu()

                elif menu_option == 2:
                    PlayerController.find()

                    menu_option = interface.player_menu()

                elif menu_option == 3:
                    PlayerController.update()

                    menu_option = interface.player_menu()

                elif menu_option == 4:
                    PlayerController.delete()

                    menu_option = interface.player_menu()

        elif option == 2:
            menu_option = interface.gm_menu()

            while menu_option != 0:
                if menu_option == 1:
                    GamemasterController.create()

                    menu_option = interface.gm_menu()

                elif menu_option == 2:
                    GamemasterController.find()

                    menu_option = interface.gm_menu()

                elif menu_option == 3:
                    GamemasterController.update()

                    menu_option = interface.gm_menu()

                elif menu_option == 4:
                    GamemasterController.delete()

                    menu_option = interface.gm_menu()

        elif option == 3:
            menu_option = interface.party_menu()

            while menu_option != 0:
                if menu_option == 1:
                    PartyController.create()

                    menu_option = interface.party_menu()

                elif menu_option == 2:
                    PartyController.find()

                    menu_option = interface.party_menu()

                elif menu_option == 3:
                    PartyController.update()

                    menu_option = interface.party_menu()

                elif menu_option == 4:
                    PartyController.delete()

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

