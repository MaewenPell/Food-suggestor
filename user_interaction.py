from display import Displayer
from sys import exit
from connector_db import Db_query
from parsing_params import Parsing_params
from Get_data_api import Get_data_api


class main_windows():
    def __init__(self):
        self.valid_choice = False
        self.main_prog()

    def main_prog(self):
        '''
            Functon used to handle the general
            execution of the program
        '''
        Displayer.print_welcome(self)
        Displayer.print_menu(self)
        self.choice_parsing(self.user_choice_checker())
        while (self.user_choice_checker() != 4):
            self.choice_parsing(self.user_choice_checker())

    def choice_parsing(self, choice):
        '''
        Function used to trigger the correct function
        depending of the user choice
        '''
        #
        # Choice of a categorie
        #
        if choice == 1:
            Db_query("print", "categorie")
            choice_cat = int(input("Please select a category : "))
            # TODO : Query BDD avec les items relatif a la catégorie
            self.user_choice_checker()
            Get_data_api(choice_cat)

        elif choice == 2:
            pass
        # --------------
        # Reset the BDD
        # --------------
        elif choice == 3:
            # TODO : loop through each tables
            Db_query("reset", "categorie")
            Parsing_params.prepare_sql_filling(self)
        # --------------
        # Leave the prog
        # --------------
        elif choice == 4:
            self.quit_prog()

    def user_choice_checker(self):
        ''' Function used to get the user choice '''
        # TODO : Enlever le 9 apres dev
        correct_choice = False
        choice = -1
        while not correct_choice:
            try:
                choice = int(input("Choisir une option : "))
                if choice > 4 or choice < 1:
                    print("Merci de choisir une option valide :")
                else:
                    return choice
            except ValueError:
                print("Merci de choisir une option valide : ")
                return -1

    def quit_prog(self):
        Displayer.quit_message(self)
        exit(0)


if __name__ == "__main__":
    main_windows = main_windows()
