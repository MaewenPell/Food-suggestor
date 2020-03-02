import pymysql

from settings_confs_files import configuration as cf

''' Database parameters '''
DB = pymysql.connect(cf.env.get("db", "host"),
                     cf.env.get("db", "username"),
                     cf.env.get("db", "password"),
                     cf.env.get("db", "schema"))

# Number of results per requests
NB_RESULTS = 100
NB_DISPLAYED = 3

# Path to the script creating the database
PATH_DB_SCRIPT = """
/Users/maewen/OpenClassrooms/Projet_5/Food-suggestor/database_management/db_creation_script.sql
"""

'''
    Creating the categories for the products
'''
CATEGORIES = ["Boissons", "Biscuits",
              "Charcuteries", "Surgelés",
              "Snacks"]

''' Tags for parsins the Open Food Fact BDD '''

TAGS_NUTRISCORE = ["nutrition_grades_tags", " nova_groups",
                   "nutriscore_grade", "nutriscore_score",
                   "nutrition_grade_fr", "nutrition_grades"]
TAGS_NAMES = ["product_name", "generic_name"]
TAGS_OTHER = ["compared_to_category"]
TAGS_STORES = ["stores"]
TAGS_LINK = ["url"]
