import pymysql
import configuration as cf

db = pymysql.connect(cf.env.get("db", "host"), cf.env.get("db", "username"),
                     cf.env.get("db", "password"), cf.env.get("db", "schema"))

cursor = db.cursor()

sql = "SELECT * FROM categorie"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
except:
    print('Ertor')

db.close()