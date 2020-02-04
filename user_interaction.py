import re
from get_categories import Get_informations


class main_windows():
    def __init__(self):
        self.valid_choice = False
        self.main_prog()

    def main_prog(self):
        '''
            Functon used to handle the general
            execution of the program
        '''
        main_message = """
         ---------------------------
        | Welcome to Food Suggestor |
         ---------------------------
        """
        print(main_message)
        cat_choice = self.user_choice()
        self.related_categories(cat_choice)

    def user_choice(self):
        '''
        Function used to display the possible
        category choice
        '''
        print("Please chose a category of product : ")
        print("1 - Drinks")
        print("2 - Biscuits and cakes")
        print("3 - Spreads")
        print("4 - Frozen food")
        print("5 - Convenience food")
        while not self.valid_choice:
            try:
                user_choice = int(input(re.sub(' +', ' ', """
                              Please type the number
                              of the wanted categorie : """)))
                if user_choice <= 5 and user_choice > 0:
                    self.valid_choice = True
                else:
                    print("Please choice among the proposed values : ")
            except ValueError:
                print("Please choice among the proposed values : ")
        return user_choice

    def related_categories(self, user_choice):
        '''
            Function used to make the correspondance
            between the user choice and the category
        '''
        # TODO : Link propre avec BDD ici --> ID
        if user_choice == 1:
            Get_informations("boissons")
        elif user_choice == 2:
            Get_informations("biscuit-et-gateaux")
        elif user_choice == 3:
            Get_informations("produits-a-tartiner")
        elif user_choice == 4:
            Get_informations("surgeles")
        elif user_choice == 5:
            Get_informations("plats-prepares")


if __name__ == "__main__":
    main_windows = main_windows()
