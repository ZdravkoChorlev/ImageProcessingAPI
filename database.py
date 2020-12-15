import psycopg2
import logging
import json
import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")

logging.basicConfig(filename='db_error.log', level=logging.DEBUG)


class Database():
    """
         The Database class is resposible for PostgreSQL connection and SQL operations
    """

    def connect(self):
        """ Connects to postgresql server

            Returns:
                connection(str): connection for the database
        """

        connection = ''

        try:
            connection = psycopg2.connect(user=POSTGRES_USER,
                                          password=POSTGRES_PASSWORD,
                                          host="db",
                                          port="5432",
                                          database=POSTGRES_DB)
        except Exception as error:
            logging.error("Connection error: ", error)

        return connection

    def create_table(self, connection):
        """ Extracts image's sha1 code from HTTP request

            Params:
                connection (str): the database connection
        """

        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS images
                (ID serial PRIMARY KEY,
                IMAGES_INFO json NOT NULL
                ); '''
        try:
            cursor.execute(create_table_query)
            connection.commit()
        except Exception as error:
            logging.error("Create table error: ", error)

    def insert_data(self, data, connection):
        """ Runs insert query against the database

            Params:
                data (str): the data that need to be inserted
                connection (str): the database connection
        """

        Database.create_table(self, connection)

        cursor = connection.cursor()
        key = data["sha1"]
        json_object = json.dumps(data, indent=2)
        insert_query = """INSERT INTO images(IMAGES_INFO) VALUES ('{0}')""".format(
            json_object)
        try:
            cursor.execute(insert_query)

            connection.commit()
        except Exception as error:
            logging.error("Insert error: ", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
