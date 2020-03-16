from settings_confs_files.settings import NB_DISPLAYED, DB, PATH_DB_SCRIPT


class SqlManagement():
    ''' Class use to retrieve and write data into the DB '''

    def create_products(self, values, cat_id):
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
        except Exception:
            DB.rollback()

    def create_categories(self, categorie_to_fill):
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
        except Exception:
            DB.rollback()

    def export_table(self, table):
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
                print(f"Error export table: {e}")

    def export_products(self, table, categorie_id):
        ''' Function used to display the products '''
        with DB.cursor() as cursor:
            sql = f"""SELECT * FROM {table} WHERE categorie_id={categorie_id}
                      LIMIT {NB_DISPLAYED};"""
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(f"Error export products: {e}")

    def export_origin_values(self, id_prod):
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
                SqlManagement.query_subsitute(self, DB, initial_values[0],
                                              initial_values[1])
            except Exception as e:
                print(f"Error export origin values: {e}")

    def query_subsitute(self, nutriscore_initial, categorie):
        with DB.cursor() as cursor:
            if nutriscore_initial == 'a':
                id_better = f"""
                SELECT * FROM db_aliments
                WHERE nutriscore <= '{nutriscore_initial}'
                AND categorie_id={categorie} LIMIT {NB_DISPLAYED};
                """
            else:
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
                print(f"Error query subst: {e}")

    def reset_bdd(self):
        ''' Function used to delete all tables '''
        print("(Ré)initialisation en cours ...")
        with DB.cursor() as cursor:
            sql = ''
            with open(PATH_DB_SCRIPT, 'r') as sql_file:
                for line in sql_file:
                    sql += line
                sql = sql.split(";")
                for line in sql:
                    try:
                        if line != "":
                            cursor.execute(line)
                            DB.commit()
                    except Exception as e:
                        print(f"Error reading the sql script {e}")
                        DB.rollback()

    def save_results_subst(self, id_old, id_subst):
        '''
            Function used to write in DB the
            substitutions products
        '''
        cursor = DB.cursor()
        sql = f"""
                INSERT IGNORE INTO substitut (id_initial_product,
                id_substitute_product)
                VALUES ('{id_old}' , '{id_subst}');
            """
        try:
            cursor.execute(sql)
            DB.commit()
        except Exception:
            DB.rollback()
            return False
        return True

    def export_products_subst(self, ids):
        '''
            Function used to export the substitutes products
        '''
        with DB.cursor() as cursor:
            sql = f"""SELECT * FROM db_aliments WHERE id={ids};"""
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(f"Error export product subst: {e}")

    def export_id_id_subst(self):
        '''
        Function used to export the id of the original product
        and the id of the choosen subst
        '''
        with DB.cursor() as cursor:
            sql = f"""SELECT id_initial_product, id_substitute_product
                      FROM substitut;"""
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(f"Error export id idsubst values: {e}")
