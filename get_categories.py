import requests


class Get_informations:
    '''
        Class use to fetch data from
        OpenFoodFact and retrieve informations
    '''
    def __init__(self):
        # TODO : change with the wanted product instead of
        #        the first one from all the products
        #
        self.manage_informations()

    def manage_informations(self):
        '''
            Routine use to call the api and receive json data
            and triggerd the different functions
        '''
        r = requests.get(
           "https://fr.openfoodfacts.org/categorie/boissons.json")
        r = r.json()

        name = self.get_name(r)
        categories = self.get_categories(r)
        store = self.get_store(r)
        link = self.get_link(r)
        nutriscore = self.get_nutriscore(r)

        print(f"""Categories are : {categories}
                  Name : {name}
                  Store : {store}
                  Link : {link}
                  Nutriscore : {nutriscore}""")

    def get_categories(self, data_to_fetch):
        '''
            Function used to trigger all the categories
        '''
        first_product = (data_to_fetch['products'][1])
        category = first_product['categories']
        return category

    def get_name(self, data_to_fetch):
        '''
            Function used to retrieve the name from the
            data
        '''
        get_elem = (data_to_fetch['products'][1])
        name = get_elem['product_name_fr']
        return name

    def get_store(self, data_to_fetch):
        '''
        Function use to get the store
        '''
        first_product = data_to_fetch['products'][1]
        store = first_product['stores']
        return store

    def get_link(self, data_to_fetch):
        '''
            Function used to get the link
            from the OPFF website
        '''
        first_product = data_to_fetch['products'][1]
        link = first_product['url']
        return link

    def get_nutriscore(self, data_to_fetch):
        ''' Function used to get the nutriscore from
            the wanted product
        '''
        first_product = data_to_fetch['products'][1]
        nutriscore = first_product['nutrition_grade_fr']
        return nutriscore


if __name__ == "__main__":
    current_search = Get_informations()
    response = current_search.manage_informations()
