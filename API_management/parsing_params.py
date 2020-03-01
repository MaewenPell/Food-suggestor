from db_management.db_interaction import Sql_management
from settings_confs_files import settings as st


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
        self.fetched_categories = st.CATEGORIES
        for cat in sorted(self.fetched_categories):
            results = Sql_management.create_categories(self, st.DB, cat)
            if not results:
                print(f"Error filling data into {cat}")
            else:
                print(f"Succes filling data into {cat}")
