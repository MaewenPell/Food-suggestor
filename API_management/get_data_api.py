import requests

from db_management.db_interaction import Sql_management
from settings_confs_files import settings as st


class Get_data_api():
    '''
        Class use to fetch data from
        OpenFoodFact and retrieve informations
    '''
    def __init__(self):
        self.tags_nutriscore = ["nutrition_grades_tags", " nova_groups",
                                "nutriscore_grade", "nutriscore_score",
                                "nutrition_grade_fr", "nutrition_grades"]
        self.tags_names = ["product_name", "generic_name"]
        self.tags_other = ["compared_to_category"]
        self.tags_stores = ["stores"]
        self.tags_link = ["url"]

    def get_tags(self):
        ''' Tags for parsing the Open Food Fact BDD '''

    def manage_products(self, categorie):
        '''
            Routine use to call the api and receive json data
            and trigger the different functions
        '''
        for current_cat in sorted(categorie):
            id_db = current_cat[0]
            cat_name = current_cat[1]

            req = (f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&\
                   tag_contains_0=contains&tag_0={cat_name}&page_size={st.NB_RESULTS}&\
                   json=true")

            # Formating the request to remove trailing whitespaces
            # due to multiline cut
            req = req.replace(' ', '')

            r = requests.get(req)
            r = r.json()
            products = r['products']

            i = 0
            for i in range(st.NB_RESULTS):
                current_product = products[i]
                name = self.get_informations(current_product,
                                             self.tags_names)
                nutriscore = self.get_informations(current_product,
                                                   self.tags_nutriscore)
                store = self.get_informations(current_product,
                                              self.tags_stores)
                link = self.get_informations(current_product,
                                             self.tags_link)

                data_products = name, nutriscore, store, link
                full_data = True
                for elem in data_products:
                    try:
                        for letters in elem:
                            if letters == "'":
                                full_data = False
                    except Exception:
                        full_data = False
                    if not elem or elem == '' or elem == 'not-applicable':
                        full_data = False

                if full_data:
                    Sql_management.create_products(self, st.DB,
                                                   data_products, id_db)

    def get_informations(self, current_product, tags):
        '''
            Function used to retrieve data_retrieved from data and check
            the integrity of the data
        '''
        empty_data = ['', 'None', 'not-apllicable', 'unknown']
        try:
            # We check all the possible tags for a wanted information
            for tag in tags:
                data_retrieved = current_product[tag]
                # If we retrieve a list of result we parse it
                if type(data_retrieved) is list:
                    for info in data_retrieved:
                        if not data_retrieved or data_retrieved in empty_data:
                            raise ValueError
                        else:
                            return info
                else:
                    # If we retrieve a single data
                    if not data_retrieved or data_retrieved in empty_data:
                        raise ValueError
                    else:
                        return data_retrieved
        except ValueError:
            pass
        except KeyError:
            pass
