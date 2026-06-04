def welcome():
    clear()

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

    input("\nPress ENTER to continue...")


def todo():
    clear()

    print("---------- TODO ----------")
    print("This module has not been implemented yet.")
    print("TODO: Feature under development.")

    input("\nPress ENTER to return...")


def main_menu():
    clear()

    print("---------- CONCLAVE MENU ----------")
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


def log_menu():
    clear()

    print("---------- CONCLAVE LOGS ----------")
    print("(1) MODULE 1")
    print("(2) MODULE 2")
    print("(3) MODULE 3")
    print("(4) MODULE 4")
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
