from display import Displayer
from sys import exit
from connector_db import Db_query
from parsing_params import Parsing_params
from Get_data_api import Get_data_api
from conf import DB


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
        self.choice_parsing()

    def choice_parsing(self):
        '''
        Function used to trigger the correct function
        depending of the user choice
        '''
        #
        # Choice of a categorie
        #
        choice_menu = -1
        choice_category = -1

        while not self.user_choice_checker(choice_menu):
            try:
                choice_menu = int(input("Choisir une fonctionnalité : "))
            except ValueError:
                print("Error, please enter only a correct number")

        if choice_menu == 1:
            results = Db_query.print_table(self, DB, 'categorie')
            Displayer.display_categories(self, results)
            # TODO : Query BDD avec les items relatif a la catégorie
            while not self.user_choice_checker(choice_category):
                try:
                    choice_category = int(input("Choisir une catégorie : "))
                except ValueError:
                    print("Error, please enter only a correct number")
            Get_data_api(choice_category)

        elif choice_menu == 2:
            pass

        # --------------
        # Reset the BDD
        # --------------
        elif choice_menu == 3:
            # TODO : loop through each tables
            Db_query.reset_bdd(self, DB)
            Parsing_params.prepare_sql_filling(self)
        # --------------
        # Leave the prog
        # --------------
        elif choice_menu == 4:
            self.quit_prog()

    def user_choice_checker(self, choice_to_check):
        ''' Function used to check the input '''
        if choice_to_check > 4 or choice_to_check < 1:
            return False
        return True

    def quit_prog(self):
        Displayer.quit_message(self)
        exit(0)


if __name__ == "__main__":
    main_windows = main_windows()
