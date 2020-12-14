import psycopg2
import logging
import json
import os

from dotenv import load_dotenv
from psycopg2 import Error

load_dotenv()

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")


def db(query):
    try:
        connection = psycopg2.connect(user=POSTGRES_USER,
                                      password=POSTGRES_PASSWORD,
                                      host="127.0.0.1",
                                      port="5432",
                                      database=POSTGRES_DB)

        cursor = connection.cursor()

        create_table_query = '''CREATE TABLE IF NOT EXISTS images
            (ID TEXT PRIMARY KEY    NOT NULL,
            IMAGES_INFO           json    NOT NULL
            ); '''

        cursor.execute(create_table_query)

        connection.commit()

        key = query["sha1"]
        json_object = json.dumps(query, indent=2)

        insert_query = """INSERT INTO images VALUES ('{0}', '{1}') ON CONFLICT DO NOTHING""".format(
            key, json_object)

        cursor.execute(insert_query)

        connection.commit()

    except (Exception, Error) as error:
        logging.error("Error while connecting to PostgreSQ", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
