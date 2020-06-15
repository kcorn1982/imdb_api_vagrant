from imdb_db_data_management.sql_management.connection_management.Imdb_DB_Conn_Manager import ImdbDBConnManager
import os

class ImdbQueryManager:

    def __init__(self):
        self.db_conn = ImdbDBConnManager(host="192.168.33.10")

    def get_all_movie_data(self):
        self.db_conn.execute_query("SELECT * FROM movies")
        return self.db_conn.return_data()


    def search_film_by_name(self, string_in_title):
        self.db_conn.execute_query("SELECT * FROM movies WHERE LOWER(movie_title) LIKE LOWER('%" + string_in_title + "%');")
        return self.db_conn.return_data()

if __name__ == '__main__':
    x = ImdbQueryManager()
    print(x.get_all_movie_data())