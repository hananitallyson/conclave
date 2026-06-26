import utils.interface as interface
import modules.conclave as conclave

if __name__ == "__main__":
    option = ""
    interface.welcome()

    while option != 0:
        option = interface.main_menu()
        conclave.run(option)
