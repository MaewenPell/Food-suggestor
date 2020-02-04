import requests


class Get_informations():
    '''
        Class use to fetch data from
        OpenFoodFact and retrieve informations
    '''
    def __init__(self, categorie):
        # TODO : Get the number of product into
        # a conf.py
        self.NB_PRODUCT = 3
        self.manage_informations(categorie)

    def manage_informations(self, categorie):
        '''
            Routine use to call the api and receive json data
            and triggerd the different functions
        '''
        r = requests.get(
            f"https://fr.openfoodfacts.org/categorie/{categorie}.json")
        r = r.json()

        for i in range(self.NB_PRODUCT):
            try:
                categories = self.get_categories(r, i)
                name = self.get_name(r, i)
                store = self.get_store(r, i)
                link = self.get_link(r, i)
                nutriscore = self.get_nutriscore(r, i)

                print(f"""Categories are : {categories}
                        Name : {name}
                        Store : {store}
                        Link : {link}
                        Nutriscore : {nutriscore}""")
            except KeyError as e:
                print("The following key is not referenced :\n",
                      e)

    def get_categories(self, data_to_fetch, current_prod):
        '''
            Function used to trigger all the categories
        '''
        current_product = (data_to_fetch['products'][current_prod])
        category = current_product['categories']
        print(category)
        return category

    def get_name(self, data_to_fetch, current_prod):
        '''
            Function used to retrieve the name from the
            data
        '''
        current_product = (data_to_fetch['products'][current_prod])
        try:
            name = current_product['product_name_fr']
            name = current_product['generic_name_fr']
        except KeyError:
            name = "Not found"
        return name

    def get_store(self, data_to_fetch, current_prod):
        '''
        Function use to get the store
        '''
        current_product = (data_to_fetch['products'][current_prod])
        store = current_product['stores']
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


# if __name__ == "__main__":
#     current_search = Get_informations()
#     response = current_search.manage_informations()
