import configuration as cf
import pymysql

''' Globals parameters '''
DB = pymysql.connect(cf.env.get("db", "host"),
                     cf.env.get("db", "username"),
                     cf.env.get("db", "password"),
                     cf.env.get("db", "schema"))
NB_RESULTS = 3
PATH_DB_SCRIPT = """
/Users/maewen/OpenClassrooms/Projet_5/Food-suggestor/draft_db_creation.sql
"""
'''
    Creating the categories for the products
'''
CATEGORIES = ["Boissons", "Biscuits",
              "Produits à tartiner", "surgelés",
              "Plats préparés"]
