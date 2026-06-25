import utils.interface as interface
import modules.player as PlayerController
import modules.gamemaster as GamemasterController
import modules.party as PartyController
import modules.log as LogController


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

        elif option == 4:
            menu_option = interface.log_menu()

            while menu_option != 0:
                if menu_option == 1:
                    LogController.list_players()

                    menu_option = interface.log_menu()

                elif menu_option == 2:
                    LogController.list_gamemasters()

                    menu_option = interface.log_menu()

                elif menu_option == 3:
                    LogController.list_parties_by_game()

                    menu_option = interface.log_menu()

                elif menu_option == 4:
                    LogController.list_all_by_date()

                    menu_option = interface.log_menu()

                elif menu_option == 5:
                    LogController.list_players_by_gamemaster()

                    menu_option = interface.log_menu()

        elif option == 0:
            interface.exit()

