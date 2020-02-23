import requests
import settings as st
from db_interraction import Sql_management


class Get_data_api():
    '''
        Class use to fetch data from
        OpenFoodFact and retrieve informations
    '''

    def manage_products(self, categorie):
        '''
            Routine use to call the api and receive json data
            and trigger the different functions
        '''
        r = requests.get(
            f"https://fr.openfoodfacts.org/categorie/{categorie}.json")
        r = r.json()
        products = r['products']

        i = 0
        for i in range(st.NB_RESULTS):
            current_product = products[i]
            name = Get_data_api.get_informations(current_product,
                                                 st.TAGS_NAMES)
            nutriscore = Get_data_api.get_informations(current_product,
                                                       st.TAGS_NUTRISCORE)
            store = Get_data_api.get_informations(current_product,
                                                  st.TAGS_STORES)
            link = Get_data_api.get_informations(current_product,
                                                 st.TAGS_LINK)
            # comparation = Get_data_api.get_informations(current_product,
            #                                            st.TAGS_OTHER)

            # -----------------------------------------------------
            # TODO : WIP / A clean après trouver une autre solution
            # -----------------------------------------------------

            data_products = name, nutriscore, store, link
            if categorie == 'Boissons':
                id_cat = 2
            elif categorie == 'Biscuits':
                id_cat = 3
            elif categorie == 'Produits à tartiner':
                id_cat = 4
            elif categorie == 'Surgelés':
                id_cat = 5
            elif categorie == 'Plats préparés':
                id_cat = 6

            full_data = True
            for elem in data_products:
                if elem is False:
                    full_data = False

            if full_data:
                Sql_management.create_products(self, st.DB,
                                               data_products, id_cat)

    def get_informations(current_product, tags):
        '''
            Function used to retrieve info from data
        '''
        try:
            for tag in tags:
                info = current_product[tag]
                if (info == 'None' or info == ''):
                    raise ValueError
                return info
        except ValueError:
            pass
        except KeyError:
            pass
        return False
