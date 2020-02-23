from display import Displayer
from sys import exit
from db_interraction import Sql_management
from parsing_params import Parsing_params
from Get_data_api import Get_data_api
from settings import DB, CATEGORIES


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

        # -------------------
        # Display categories
        # and products
        # -------------------

        if choice_menu == 1:
            results = Sql_management.export_table(self, DB, 'categorie')
            Displayer.display_categories(self, results)
            while not self.user_choice_checker(choice_category):
                try:
                    choice_category = int(input("Choisir une catégorie : "))
                    results = Sql_management.export_products(self, DB,
                                                             'db_aliments',
                                                             choice_category)
                    Displayer.display_products(self, results)
                except ValueError:
                    print("Error, please enter only a correct number")

        # --------------------------
        # Display substitue products
        # --------------------------
        elif choice_menu == 2:
            pass

        # --------------
        # Reset the BDD
        # --------------
        elif choice_menu == 3:
            # TODO : loop through each tables and categories
            # 1st : We delete and recreate the BDD
            Sql_management.reset_bdd(self, DB)
            # 2nd : We create the categories from config.py
            Parsing_params.cat_filling(self)
            # 3rd we loop through the result and adding them into the BDD
            # TODO : automatize the categories filling
            for category in CATEGORIES:
                Get_data_api.manage_products(self, category)
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
