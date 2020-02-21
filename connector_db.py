import pymysql
from display import Displayer


class Db_query():
    ''' Class use to retrieve and write data into the DB '''
    def create_products(self, DB):
        '''
        Categorie use to fill the product table :
        schema is : ID, categorie_ID, nom_aliment, magasin, lien, nutriscore
        '''
        pass

    def create_categories(self, DB, categorie_to_fill):
        cursor = DB.cursor()

        sql = f"""INSERT INTO categorie (related_category, id_off)
                    VALUES ('{categorie_to_fill}', '{categorie_to_fill}');
                """
        try:
            cursor.execute(sql)
            DB.commit()
            print(f"Sucess filling {categorie_to_fill}")
        except Exception as e:
            print(f"Error inserting data : {e}")
            DB.rollback()
        # self.db.close()

    def print_table(self, DB, table):
        ''' Function used to display the content of the DB '''
        with DB.cursor() as cursor:
            sql = f"SELECT * FROM {table}"
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(e)

    def reset_bdd(self, DB):
        ''' Function used to delete all tables '''
        # TODO Loop through each tables
        with DB.cursor() as cursor:
            sql = ''
            with open('draft_db_creation.sql', 'r') as sql_file:
                for line in sql_file:
                    sql += line
                sql = sql.split(";")
                for line in sql:
                    try:
                        cursor.execute(line)
                        DB.commit()
                    except Exception as e:
                        print(f"{e} occured at {line}")
                        DB.rollback()
