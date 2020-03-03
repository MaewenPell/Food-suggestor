class Displayer():
    '''
        Class used to handle all the messages
        that will be display to the user
    '''

    def print_welcome(self):
        print("""
         ---------------------------
        | Welcome to Food Suggestor |
         ---------------------------
        """)

    def print_menu(self):
        print(
            """
            \t ------------------------------------
            \t Menu principal :
            \t 1- Choisir une catégorie
            \t 2- Afficher les produits substitués
            \t 3- Réinitialiser la base de donnée
            \t 4- Quitter le programme
            \t ------------------------------------
            \n
            """)

    def quit_message(self):
        print(
            """
             -------------------------------------------------------
            | Merci d'avoir utiliser Food suggestor pour contribuer |
            | https://github.com/MaewenPell/Food-suggestor          |
             -------------------------------------------------------
            """
        )

    def display_categories(self, categories):
        ''' Function used to display the categories '''
        for elem in categories:
            id_cat = elem[0]
            nom = elem[1]
            print(f"{id_cat} - {nom}")

    def display_sep():
        print('\n\n')

    def display_subsitute_message():
        print("Voila les produits substitués : \n")

    def display_products(self, results):
        '''
            Display information from the different categories
            depending on the user choice
        '''
        for products in results:
            id_prod = products[0]
            name = products[2]
            nutriscore = products[5]
            store = products[3]
            link = products[4]
            print("-----------------------------")
            print(f"Choix n°{id_prod}")
            print(f"Nom du produit : {name}")
            print(f"Nutriscore : {nutriscore}")
            print(f"Magasin : {store}")
            print(f"Lien : {link}")
            print("-------------")
