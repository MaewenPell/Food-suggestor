import configuration as cf
import pymysql

''' Globals parameters '''
DB = pymysql.connect(cf.env.get("db", "host"),
                     cf.env.get("db", "username"),
                     cf.env.get("db", "password"),
                     cf.env.get("db", "schema"))
NB_RESULTS = 20
PATH_DB_SCRIPT = """
/Users/maewen/OpenClassrooms/Projet_5/Food-suggestor/db_creation_scripts.sql
"""


'''
    Creating the categories for the products
'''
CATEGORIES = ["Boissons", "Biscuits",
              "Produits à tartiner", "Surgelés",
              "Plats préparés"]

''' Tags for parsins the Open Food Fact BDD '''

TAGS_NUTRISCORE = ["nutrition_grades_tags", " nova_groups",
                   "nutriscore_grade", "nutriscore_score",
                   "nutrition_grade_fr", "nutrition_grades"]
TAGS_NAMES = ["product_name_fr",
              "product_name", "generic_name"]
TAGS_OTHER = ["compared_to_category"]
TAGS_STORES = ["stores"]
TAGS_LINK = ["url"]
