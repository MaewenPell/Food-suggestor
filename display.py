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
            Menu principal :
            \t 1- Choisir une catégorie
            \t 2- Afficher les produits substitués
            \t 3- Réinitialiser la base de donnée
            \t 4- Quitter le programme
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

    def display_products(self, results):
        '''
            Display information from the different categories 
            depending on the user choice
        '''
        for products in results:
            name = products[2]
            nutriscore = products[3]
            store = products[4]
            link = products[5]
            print("-------------")
            print(f"Nom du produit : {name}")
            print(f"Nutriscore : {nutriscore}")
            print(f"Magasin : {store}")
            print(f"Lien : {link}")
            print("-------------")
