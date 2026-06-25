from utils import database
from utils import entry
from utils import interface


def create():
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


def find():
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


def update():
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

                return None

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


def delete():
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
