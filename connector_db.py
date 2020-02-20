import pymysql
import configuration as cf
from display import Displayer


class Db_query():
    ''' Class use to retrieve and write data into the DB '''
    def __init__(self, action, additionnal_param=None):
        self.db = pymysql.connect(cf.env.get("db", "host"),
                                  cf.env.get("db", "username"),
                                  cf.env.get("db", "password"),
                                  cf.env.get("db", "schema"))
        if action == 'fill_categories':
            self.create_categories(additionnal_param)
        elif action == 'reset':
            self.reset_bdd(additionnal_param)
        elif action == 'print':
            self.print_table(additionnal_param)
        elif action == 'fill_products':
            self.create_products()

    def create_products(self):
        ''' 
        Categorie use to fill the product table :
        schema is : ID, categorie_ID, nom_aliment, magasin, lien, nutriscore
        '''
        pass

    def create_categories(self, categorie_to_fill):
        cursor = self.db.cursor()

        sql = f"""INSERT INTO categorie (related_category, id_off)
                    VALUES ('{categorie_to_fill}', '{categorie_to_fill}');
                """
        try:
            cursor.execute(sql)
            self.db.commit()
            print(f"Sucess filling {categorie_to_fill}")
        except Exception as e:
            print(f"Error inserting data : {e}")
            self.db.rollback()
        # self.db.close()

    def print_table(self, table):
        ''' Function used to display the content of the DB '''
        with self.db.cursor() as cursor:
            sql = f"SELECT * FROM {table}"
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                Displayer.display_categories(self, results)
            except Exception as e:
                print(e)

    def reset_bdd(self, table):
        ''' Function used to delete all rows of a table '''
        with self.db.cursor() as cursor:
            sql = f"DELETE FROM {table};"
            sql1 = f"ALTER TABLE {table} AUTO_INCREMENT = 1;"
            try:
                cursor.execute(sql)
                self.db.commit()
                cursor.execute(sql1)
                self.db.commit()
            except Exception as e:
                print(f"""Error reseting BDD
                the following error occured {e}""")
                self.db.rollback()
