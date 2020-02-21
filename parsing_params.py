from conf import CATEGORIES, DB
from connector_db import Db_query


class Parsing_params():
    '''
    Class used to parse the parameters and
    trigger the BDD filling functions
    '''

    def prepare_sql_filling(self):
        '''
        Fuction used to get the name of the categories
        and give these informations to Db query to
        fill the bdd
        '''
        self.fetched_categories = CATEGORIES
        for cat in sorted(self.fetched_categories):
            # Db_query('fill_categories', cat)
            Db_query.create_categories(self, DB, cat)


if __name__ == "__main__":
    Parsing_params()
