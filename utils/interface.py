from . import helper


def wait():
    input("\nPress ENTER to continue...")


def welcome():
    helper.clear()

    print(r"""
 ██████╗ ██████╗ ███╗   ██╗ ██████╗██╗      █████╗ ██╗   ██╗███████╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝██║     ██╔══██╗██║   ██║██╔════╝
██║     ██║   ██║██╔██╗ ██║██║     ██║     ███████║██║   ██║█████╗
██║     ██║   ██║██║╚██╗██║██║     ██║     ██╔══██║╚██╗ ██╔╝██╔══╝
╚██████╗╚██████╔╝██║ ╚████║╚██████╗███████╗██║  ██║ ╚████╔╝ ███████╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝

═══════════════════════════════════════════════════════════════════════
                     Welcome to CONCLAVE
═══════════════════════════════════════════════════════════════════════
""")

    wait()


def exit():
    print("\nExiting...\n")


def todo():
    helper.clear()

    header("TODO")
    print("This module has not been implemented yet.")
    print("TODO: Feature under development.")

    input("\nPress ENTER to return...")


def main_menu():
    helper.clear()

    header("CONCLAVE MENU")
    print("(1) PLAYERS")
    print("(2) GAMEMASTERS")
    print("(3) PARTIES")
    print("(4) LOGS")
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
    helper.clear()

    header("PLAYERS")
    print("(1) NEW PLAYER")
    print("(2) FIND PLAYER")
    print("(3) UPDATE PLAYER")
    print("(4) DELETE PLAYER")
    print("(0) BACK TO MENU")

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
    helper.clear()

    header("GAMEMASTERS")
    print("(1) NEW GAMEMASTER")
    print("(2) FIND GAMEMASTER")
    print("(3) UPDATE GAMEMASTER")
    print("(4) DELETE GAMEMASTER")
    print("(0) BACK TO MENU")

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
    helper.clear()

    header("PARTIES")
    print("(1) NEW PARTY")
    print("(2) FIND PARTY")
    print("(3) UPDATE PARTY")
    print("(4) DELETE PARTY")
    print("(0) BACK TO MENU")

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


def log_menu():
    helper.clear()

    header("CONCLAVE LOGS")
    print("(1) LIST PLAYERS")
    print("(2) LIST GAMEMASTERS")
    print("(3) LIST PARTIES BY GAME")
    print("(4) LIST BY CREATION DATE")
    print("(5) LIST PLAYERS BY GAMEMASTER")
    print("(0) BACK TO MENU")

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
        case "5":
            option = 5
        case _:
            option = 1

    return option


def header(title):
    helper.clear()

    print(f"-------------- {title} --------------\n")


def confirm():
    i = input("CONTINUE? (Y/N): ").upper()

    if i == "Y" or i == "":
        choice = True
    else:
        choice = False

    return choice
