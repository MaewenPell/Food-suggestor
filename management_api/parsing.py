from db_management.db_interaction import SqlManagement
from settings_confs_files import settings as st


class ParsingParams():
    '''
    Class used to parse parameters and trigger sql management
    '''

    def cat_filling(self):
        '''
        Fuction used to get the name of the categories
        and trigger Sql_management Class to fill the bdd
        '''
        fetched_categories = st.CATEGORIES
        for cat in sorted(fetched_categories):
            results = SqlManagement.create_categories(self, cat)
            if not results:
                print(f"Error creating {cat}")
