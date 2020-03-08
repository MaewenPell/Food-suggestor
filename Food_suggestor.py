from os import system
from sys import exit

from api_management.get_data_api import Api_manager
from api_management.parsing import Parsing_params
from db_management.db_interaction import Sql_management
from user_interraction.display import Displayer


class main_windows():
    def __init__(self):
        self.displayer = Displayer()
        self.sql_mgt = Sql_management()
        self.displayer.print_welcome()
        self.api_worker = Api_manager()
        self.main()

    def main(self):
        '''
            Functon used to handle the general
            execution of the program
        '''
        self.valid_choice = False
        self.displayer.print_menu()
        self.choice_parsing()

    def choice_parsing(self):
        '''
        Function used to trigger the correct function
        depending of the user choice
        '''

        choice_menu = -1

        # While the user didn't enter a valid choice
        while not self.num_check(choice_menu):
            try:
                choice_menu = int(input("Choisir une action : "))
            except ValueError:
                print("Erreur, merci de choisir une entrée valable")

        if choice_menu == 1:
            self.display_prod_by_cat()

        if choice_menu == 2:
            self.dislpay_substitutes()

        elif choice_menu == 3:
            self.reset_db()

        elif choice_menu == 4:
            self.quit_prog()

        self.main()

    def display_prod_by_cat(self):
        '''
            Function used to display the content of the different
            cat so the user can choose a id_prod to subsitute
        '''
        # First display the differents categories
        results = self.sql_mgt.export_table('categorie')
        self.displayer.display_categories(results)

        # We ask the user to choose a category
        choice_category = -1
        while not self.num_check(choice_category):
            try:
                # We display the available categories and ask for a choice
                try:
                    choice_category = int(input(
                        "Choisir une catégorie d'aliments : "))
                except ValueError:
                    print("Merci d'entrer une valeur existante")
                # Querying the DB
                prod_by_cat = self.sql_mgt.export_products('db_aliments',
                                                           choice_category)
                # Display the products of this category
                self.displayer.display_products(prod_by_cat)
                # Trigger the function where the user choose the id_product to
                # substiute
                self.alim_to_sub(prod_by_cat)
            except Exception as e:
                print(f"Error retriving the data associated to this cat {e}")
                return False

    def alim_to_sub(self, prod_by_cat):
        '''
            Function used to retrieve the wanted id_product to be substitue
            and display the subsitute
        '''
        try:
            # we retrieve the id_product to subsitute
            # TODO : check if the id exist
            id_prod = int(input(
                "Choisir un id de produit à substituer : "))
            system('cls||clear')

            self.displayer.display_subsitute_message()
            # We get the nutriscore and the cat of this id_product
            origin_values = self.sql_mgt.export_origin_values(id_prod)
            old_nutriscore = origin_values[0][0]
            cat = origin_values[0][1]
            # We query and retrieve the possible subsitute
            data_subst = self.sql_mgt.query_subsitute(old_nutriscore,
                                                      cat)
            # We display the information about the subsituate id_product
            self.displayer.display_products(data_subst)
            self.save_into_db(id_prod, data_subst[0][0])
        except ValueError:
            print("Merci de choisir un nombre correspondant à une entrée")

    def dislpay_substitutes(self):
        '''
            Function used to display the initial product and the
            saved subsitute
        '''
        results = self.sql_mgt.export_id_id_subst()
        system('cls||clear')
        for elem in results:
            id_orig = elem[0]
            id_susbst = elem[1]
            print("\nProduit initialement choisi : \n")
            orig_data = self.sql_mgt.export_products_subst(id_orig)
            self.displayer.display_products(orig_data)
            print("\n Produit substitué : \n")
            subst_data = self.sql_mgt.export_products_subst(id_susbst)
            self.displayer.display_products(subst_data)

    def reset_db(self):
        '''
            Class used to reset the DB
        '''
        # 1st : We delete and recreate the BDD
        self.sql_mgt.reset_bdd()
        # 2nd : We create the categories from config.py
        Parsing_params.cat_filling(self)
        # 3rd we loop through the result and adding them into the BDD
        categories_sql = self.sql_mgt.export_table('categorie')
        self.api_worker.manage_products(categories_sql)

    def save_into_db(self, id_old, data_subst):
        '''
            Function used to save the result in the DB
        '''
        save = -1
        save = input("Sauvegarder la subsitution ? (O/N) : ")
        save = save.upper()
        while save != 'O' and save != 'N':
            save = input("Merci d'entrer 'O' ou 'N' : ")
            save = save.upper()
        if save == 'O':
            self.sql_mgt.save_results_subst(id_old,
                                            data_subst)

    def num_check(self, choice_to_check):
        ''' Function used to check the input '''
        if choice_to_check > 4 or choice_to_check < 1:
            return False
        return True

    def quit_prog(self):
        self.displayer.quit_message()
        exit(0)


if __name__ == "__main__":
    main_windows = main_windows()
