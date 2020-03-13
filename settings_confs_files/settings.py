import pymysql

from settings_confs_files import configuration as cf

# Database parameters
DB = pymysql.connect(cf.env.get("db", "host"),
                     cf.env.get("db", "username"),
                     cf.env.get("db", "password"),
                     cf.env.get("db", "schema"))

# Number of results per requests
NB_RESULTS = 200
NB_DISPLAYED = 5

# Path to the script creating the database
PATH_DB_SCRIPT = "db_management/db_creation_script.sql"

# Creating the categories for the products
CATEGORIES = ["Boissons", "Biscuits",
              "Charcuteries", "Surgelés",
              "Snacks"]
