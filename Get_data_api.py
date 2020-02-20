import requests
import conf


class Get_data_api():
    '''
        Class use to fetch data from
        OpenFoodFact and retrieve informations
    '''
    def __init__(self, categorie):
        self.categorie = categorie
        self.manage_informations()

    def manage_informations(self):
        '''
            Routine use to call the api and receive json data
            and trigger the different functions
        '''
        r = requests.get(
            f"https://fr.openfoodfacts.org/categorie/{self.categorie}.json")
        r = r.json()

        i = 0
        for i in range(conf.NB_RESULTS):
            try:
                complete = True
                categories = self.get_categories(r, i)
                name = self.get_name(r, i)
                store = self.get_store(r, i)
                link = self.get_link(r, i)
                nutriscore = self.get_nutriscore(r, i)
                all_cat = [categories, name,
                           store, link, nutriscore]
                for elem in enumerate(all_cat):
                    if (elem is None or elem == ''):
                        complete = False


                if complete:
                    print(f"""Categories : {categories}
                            -------------------------------
                            Name : {name}
                            -------------------------------
                            Store : {store}
                            -------------------------------
                            Link : {link}
                            -------------------------------
                            Nutriscore : {nutriscore}
                            -------------------------------
                            """)
            except KeyError as e:
                print("The following key is not referenced :\n",
                      e)
            except IndexError:
                print("Not enough data")

    def get_categories(self, data_to_fetch, current_prod):
        '''
            Function used to trigger all the categories
        '''
        current_product = (data_to_fetch['products'][current_prod])
        category = current_product['categories']
        return category

    def get_name(self, data_to_fetch, current_prod):
        '''
            Function used to retrieve the name from the
            data
        '''
        current_product = (data_to_fetch['products'][current_prod])
        try:
            try:
                name = current_product['product_name_fr']
            except KeyError:
                name = current_product['product_name']
        except KeyError:
            name = "None"
        if name != '':
            return name
        else:
            return "None"

    def get_store(self, data_to_fetch, current_prod):
        '''
        Function use to get the store
        '''
        current_product = (data_to_fetch['products'][current_prod])
        try:
            store = current_product['stores']
        except KeyError:
            store = 'None'
        if store == '':
            store = 'None'
        return store

    def get_link(self, data_to_fetch, current_prod):
        '''
            Function used to get the link
            from the OPFF website
        '''
        current_product = (data_to_fetch['products'][current_prod])
        link = current_product['url']
        return link

    def get_nutriscore(self, data_to_fetch, current_prod):
        ''' Function used to get the nutriscore from
            the wanted product
        '''
        current_product = data_to_fetch['products'][current_prod]
        try:
            nutriscore = current_product['nutrition_grade_fr']
        except KeyError:
            nutriscore = current_product['nutrition_grades_tags']

        return nutriscore
