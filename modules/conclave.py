import utils.interface as interface
import modules.player as player
import modules.gamemaster as gamemaster
import modules.party as party
import modules.log as log


def run(option):
    if option == 1:
      menu_option = interface.player_menu()
      while menu_option != 0:
          menu_option = player.run(menu_option)

    elif option == 2:
      menu_option = interface.gm_menu()
      while menu_option != 0:
          menu_option = gamemaster.run(menu_option)

    elif option == 3:
      menu_option = interface.party_menu()
      while menu_option != 0:
          menu_option = party.run(menu_option)

    elif option == 4:
      menu_option = interface.log_menu()
      while menu_option != 0:
          menu_option = log.run(menu_option)

    elif option == 0:
      interface.exit()
