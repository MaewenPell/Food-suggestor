from settings import CATEGORIES, DB
from db_interraction import Sql_management


class Parsing_params():
    '''
    Class used to parse the parameters and
    trigger the BDD filling functions
    '''

    def cat_filling(self):
        '''
        Fuction used to get the name of the categories
        and trigger Sql_management Class to
        fill the bdd
        '''
        self.fetched_categories = CATEGORIES
        for cat in sorted(self.fetched_categories):
            results = Sql_management.create_categories(self, DB, cat)
            if not results:
                print(f"Error filling data into {cat}")
            else:
                print(f"Succes filling data into {cat}")


if __name__ == "__main__":
    Parsing_params()
