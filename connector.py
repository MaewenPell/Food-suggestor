import pymysql
import configuration as cf
from conf import CATEGORIES


class Db_query():
    ''' Class use to retrieve and write data into the DB '''
    def __init__(self):
        self.db = pymysql.connect(cf.env.get("db", "host"),
                                  cf.env.get("db", "username"),
                                  cf.env.get("db", "password"),
                                  cf.env.get("db", "schema"))

    def create_categories(self):
        cursor = self.db.cursor()
        for cat in CATEGORIES:
            related_cat = CATEGORIES[cat]['related_cat']
            id_off = CATEGORIES[cat]['id_off']
            sql = f"""INSERT INTO categorie
                     VALUES (NULL, '{related_cat}', '{id_off}');
                    """
            print(sql)
            try:
                cursor.execute(sql)
                self.db.commit()
            except Exception as e:
                print(f"Error inserting data : {e}")
                self.db.rollback()
        self.db.close()

    def print_db(self):
        # TODO : Debug
        cursor = self.db.cursor()
        sql = "SELECT * FROM main_db_food_suggestor.categorie"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
        except Exception as e:
            print(f'{e}')


if __name__ == "__main__":
    a = Db_query()
    a.create_categories()
    a.print_db()
