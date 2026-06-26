import utils.interface as interface
import modules.player as Player
import modules.gamemaster as Gamemaster
import modules.party as Party
import modules.log as Log


def run(option):
    if option == 1:
      menu_option = interface.player_menu()
      while menu_option != 0:
          menu_option = Player.crud(menu_option)

    elif option == 2:
      menu_option = interface.gm_menu()
      while menu_option != 0:
          menu_option = Gamemaster.crud(menu_option)

    elif option == 3:
      menu_option = interface.party_menu()
      while menu_option != 0:
          menu_option = Party.crud(menu_option)

    elif option == 4:
      menu_option = interface.log_menu()
      while menu_option != 0:
          menu_option = Log.module(menu_option)

    elif option == 0:
      interface.exit()
