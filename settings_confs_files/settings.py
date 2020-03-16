import pymysql

from settings_confs_files import configuration as cf

# Database parameters that we load from the environnement.txt
DB = pymysql.connect(cf.env.get("db", "host"),
                     cf.env.get("db", "username"),
                     cf.env.get("db", "password"),
                     cf.env.get("db", "schema"))

# Number of results that we load from the OFF open DB
# for EACH category
NB_RESULTS = 200

# Number of products that we display on the screen
# (substitutes and product in categories)
NB_DISPLAYED = 5

# Path of the script to create the database
PATH_DB_SCRIPT = "db_management/db_creation_script.sql"

# Categories that we'll load from the OFF DB
CATEGORIES = ["Boissons", "Biscuits",
              "Confiseries", "Surgelés",
              "Snacks"]
