from sys import exit

from API_management.get_data_api import Get_data_api
from database_management.db_interraction import Sql_management
from settings_confs_files.parsing_params import Parsing_params
from settings_confs_files.settings import DB
from user_interaction.display import Displayer


class main_windows():
    def __init__(self):
        self.valid_choice = False
        self.api_worker = Get_data_api()
        self.main_prog()
        Displayer.print_welcome(self)

    def main_prog(self):
        '''
            Functon used to handle the general
            execution of the program
        '''
        Displayer.print_menu(self)
        self.choice_parsing()

    def choice_parsing(self):
        '''
        Function used to trigger the correct function
        depending of the user choice
        '''

        # ---------------------
        # Choice of a categorie
        # ---------------------

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
            while not self.user_choice_checker(choice_category):
                try:
                    choice_category = int(input("Choisir une catégorie : "))
                    results = Sql_management.sort_product(self, DB,
                                                          choice_category)
                    Displayer.display_products(self, results)
                except ValueError:
                    print("Error, please enter only a correct number")

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
            categories_sql = Sql_management.export_table(self, DB, 'categorie')
            self.api_worker.manage_products(categories_sql)

        # --------------
        # Leave the prog
        # --------------

        elif choice_menu == 4:
            self.quit_prog()

        self.main_prog()

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
