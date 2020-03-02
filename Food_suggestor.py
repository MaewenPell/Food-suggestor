from sys import exit

from API_management.get_data_api import Api_manager
from API_management.parsing import Parsing_params
from db_management.db_interaction import Sql_management
from settings_confs_files.settings import DB
from user_interraction.display import Displayer


class main_windows():
    def __init__(self):
        self.valid_choice = False
        self.api_worker = Api_manager()
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

        # While the user didn't enter a valid choice
        while not self.user_choice_checker(choice_menu):
            try:
                choice_menu = int(input("Choisir une action : "))
            except ValueError:
                print("Erreur, merci de choisir une entrée valable")

        # ---------------------------------
        # Display Aliments for subsitution
        # 1- Choice cat
        #
        # TODO :
        # 2- Choice Alim √
        # 3- Display substitue
        # 4- Save result in BDD
        # ---------------------------------

        if choice_menu == 1:
            self.display_alim_for_subst()

        # --------------------------
        # Display substitue products
        # --------------------------

        # TODO : A retravailler

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

    def display_alim_for_subst(self):
        '''
            Function used to display the categories
            and the aliments from the BDD
        '''
        results = Sql_management.export_table(self, DB, 'categorie')
        Displayer.display_categories(self, results)

        choice_category = -1
        while not self.user_choice_checker(choice_category):
            try:
                # First we display the available categories
                # and we display the associate product
                choice_category = int(input(
                        "Choisir une catégorie d'aliments : \n"))
                results = Sql_management.export_products(self, DB,
                                                         'db_aliments',
                                                         choice_category)
                Displayer.display_products(self, results)

                # Secondly we choose a product to subsitute
                prod = int(input(
                    "Choisir un produit à substituer : "))
                # We retrieve the nutriscore and the cat of this product
                initial_values = Sql_management.export_origin_values(self,
                                                                     DB,
                                                                     prod)
                # We query and retrieve the possible subsitutes
                sub_id = Sql_management.query_subsitute(self, DB,
                                                        initial_values[0][0],
                                                        initial_values[0][1])
                # We display them
                Displayer.display_products(self, sub_id)
            except ValueError:
                print("Merci de choisir un nombre \
                       correspondant à une entrée")

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
