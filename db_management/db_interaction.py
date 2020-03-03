from settings_confs_files.settings import NB_DISPLAYED, DB


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
            print(f"{sql}")
            DB.rollback()

    def create_categories(self, DB, categorie_to_fill):
        '''
            Function used to create the categorie into the DB depends
            of the categories we fill into settings
        '''
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
        '''
            Function used to export sql results
            of the content of the DB
        '''
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
            sql = f"""SELECT * FROM {table} WHERE categorie_id={categorie_id}
                      LIMIT {NB_DISPLAYED};"""
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(e)

    def export_origin_values(self, DB, id_prod):
        '''
            Function used to return the nutriscore and the
            categorie id from the requested product
        '''
        with DB.cursor() as cursor:
            sql = f"""
            SELECT nutriscore, categorie_id FROM
            db_aliments WHERE id={id_prod};"""
            try:
                cursor.execute(sql)
                initial_values = cursor.fetchall()
                return initial_values
                Sql_management.query_subsitute(self, DB, initial_values[0],
                                               initial_values[1])
            except Exception as e:
                print(e)

    def query_subsitute(self, db, nutriscore_initial, categorie):
        with DB.cursor() as cursor:
            id_better = f"""
            SELECT * FROM db_aliments
            WHERE nutriscore < '{nutriscore_initial}'
            AND categorie_id={categorie} LIMIT {NB_DISPLAYED};
            """
            try:
                cursor.execute(id_better)
                results_sub = cursor.fetchall()
                return results_sub
            except Exception as e:
                print(e)

    def reset_bdd(self, DB):
        ''' Function used to delete all tables '''
        with DB.cursor() as cursor:
            sql = ''
            with open('db_management/db_creation_script.sql', 'r') as sql_file:
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

    def save_results_subst(self, id_old, id_new):
        '''
            Function used to write in DB the
            substitutions products
        '''
        for elem in sorted(id_new):
            cursor = DB.cursor()
            sql = f"""
                    INSERT INTO substitut (id_initial_product,
                    id_substitute_product)
                    VALUES ('{id_old}' , '{elem}');
                """
            try:
                cursor.execute(sql)
                DB.commit()
            except Exception as e:
                print(f"Error inserting data: {e}")
                print(f"{sql}")
                DB.rollback()
                return False

    def export_products_subst(self, ids):
        ''' Function used to display the substitue products '''
        with DB.cursor() as cursor:
            sql = f"""SELECT * FROM db_aliments WHERE id={ids};"""
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(e)
