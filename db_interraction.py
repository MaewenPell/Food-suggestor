
class Sql_management():
    ''' Class use to retrieve and write data into the DB '''

    def create_products(self, DB, values, cat_id):
        '''
        Categorie use to fill the product table Schema is:
        db_aliments : categorie_id, alim_name, store, website_link, nutriscore
        '''
        name, nutriscore = values[0], values[1][0],
        store, link = values[2], values[3]

        cursor = DB.cursor()

        sql = f"""
                INSERT INTO db_aliments (categorie_id, alim_name, store,
                                        website_link, nutriscore)
                VALUES ({cat_id} , '{name}', '{store}',
                        '{link}', '{nutriscore}');
            """
        try:
            cursor.execute(sql)
            DB.commit()
            return True
        except Exception as e:
            print(f"Error inserting data: {e}")
            print(f"id = {cat_id}")
            DB.rollback()

    def create_categories(self, DB, categorie_to_fill):
        cursor = DB.cursor()

        sql = f"""INSERT INTO categorie (name)
                    VALUES ('{categorie_to_fill}');
                """
        try:
            cursor.execute(sql)
            DB.commit()
            return True
        except Exception as e:
            print(f"Error inserting data : {e}")
            DB.rollback()
        # self.db.close()

    def export_table(self, DB, table):
        ''' Function used to display the content of the DB '''
        with DB.cursor() as cursor:
            sql = f"SELECT * FROM {table}"
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(e)

    def export_products(self, DB, table, categorie_id):
        ''' Function used to display the products '''
        with DB.cursor() as cursor:
            sql = f"SELECT * FROM {table} WHERE categorie_id={categorie_id};"
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
            with open('db_creation_script.sql', 'r') as sql_file:
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
