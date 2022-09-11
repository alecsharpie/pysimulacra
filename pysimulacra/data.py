import sqlite3
import pandas as pd


class SimulacraData:

    def __init__(self, sqlite_path):
        """connect to sql file"""
        self.path = sqlite_path
        self.conn = sqlite3.connect(self.path)
        self.all_table_names = self.fetch_table_names()

    def fetch_table_names(self):
        """get all table names"""

        cursorObj = self.conn.cursor()

        cursorObj.execute('SELECT name from sqlite_master where type= "table"')

        return [
            table[0] for table in cursorObj.fetchall()
            if not table[0].startswith('sqlite_')
        ]

    def fetch_all_data(self):
        """create a dictionary containing all tables from db
        key = table_name
        value = pd.DataFrame tables"""

        data = {}

        base_query = 'SELECT * from '

        all_data = {
            table_name: pd.read_sql_query(f'{base_query}{table_name}',
                                          self.conn)
            for table_name in self.all_table_names
        }

        print('Table : col1, col2, col3, ...')
        print('----------')
        for key, data in all_data.items():
            print(key, ' : ', ', '.join(data.columns))

        return all_data

    def get_image_paths_and_prompts(self):

        query = """
            SELECT images.id AS img_id, generations.prompt AS gen_prompt, paths.path as img_path FROM images
            JOIN generations ON images.gid = generations.id
            JOIN paths ON images.id = paths.iid
            """
        return pd.read_sql_query(query, self.conn)

    def get_prompts_and_ratings(self):

        query = """
            SELECT images.id AS img_id, generations.prompt AS img_prompt, AVG(ratings.rating) AS img_rating FROM images
            JOIN generations ON images.gid = generations.id
            JOIN ratings ON images.id = ratings.iid
            GROUP BY img_prompt
            """
        return pd.read_sql_query(query, self.conn)


    def get_image_paths_and_prompts_and_ratings(self):

        query = """
            SELECT images.id AS img_id, generations.prompt AS img_prompt, paths.path as img_path, ratings.rating AS img_rating FROM images
            JOIN generations ON images.gid = generations.id
            JOIN ratings ON images.id = ratings.iid
            JOIN paths ON images.id = paths.iid
            """
        return pd.read_sql_query(query, self.conn)
