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
            \t 9- Dev : Remplier cat
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
        for elem in categories:
            id_cat = elem[0]
            nom = elem[1]
            print(f"{id_cat} - {nom}")