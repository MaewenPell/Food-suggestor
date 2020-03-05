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

        choice_menu = -1

        # While the user didn't enter a valid choice
        while not self.user_choice_checker(choice_menu):
            try:
                choice_menu = int(input("Choisir une action : "))
            except ValueError:
                print("Erreur, merci de choisir une entrée valable")

        # ---------------------
        # Choice of a categorie
        # ---------------------

        if choice_menu == 1:
            id_old, id_subst = self.display_alim_for_subst()
            save = 'e'
            save = input("Save the results in the databse ? (Y/N) : ")
            while save != 'Y' and save != 'N':
                save = input("Please enter 'Y' or 'N' : ")
                save = save.upper()
            if save == 'Y':
                res_q = Sql_management.save_results_subst(self,
                                                          id_old,
                                                          id_subst)
                if not res_q:
                    print('\n XX Error filling DB XX\n')
                else:
                    print("\n !! Succes filling DB !! \n")

        # --------------------------
        # Display substitue products
        # --------------------------

        if choice_menu == 2:
            i = 0
            sql = Sql_management.export_table(self, DB, 'substitut')
            sql = list(sql)
            subsitute_products = [elem[2] for elem in sql]

            inital_prod = list(dict.fromkeys([elem[1] for elem in sql]))

            # Retrieve original products
            for elem in inital_prod:
                origin_data = Sql_management.export_products_subst(self,
                                                                   inital_prod[i])
                print("-------------- Original product : ------------------ ")
                Displayer.display_products(self, origin_data)

                print("------------- Substitutes ---------------------------")
                for elem in subsitute_products:
                    current_sub = Sql_management.export_products_subst(self,
                                                                       elem)
                    Displayer.display_products(self, current_sub)
                i += 1
                print("------------- Next product -------------")



        # --------------
        # Reset the BDD
        # --------------

        elif choice_menu == 3:
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
                Displayer.display_sep()

                # Secondly we choose a product to subsitute
                prod = int(input(
                    "Choisir un produit à substituer : "))
                Displayer.display_sep()
                Displayer.display_subsitute_message()
                # We retrieve the nutriscore and the cat of this product
                origin_prod = Sql_management.export_origin_values(self,
                                                                  DB,
                                                                  prod)
                old_nutriscore = origin_prod[0][0]
                cat = origin_prod[0][1]
                # We query and retrieve the possible subsitutes
                substitutes = Sql_management.query_subsitute(self, DB,
                                                             old_nutriscore,
                                                             cat)
                substitutes = list(substitutes)
                id_subst = [elem[0] for elem in substitutes]
                # We display them
                Displayer.display_products(self, substitutes)
                return prod, id_subst
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
