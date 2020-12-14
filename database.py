import psycopg2
import logging
import json

from psycopg2 import Error


def db(query):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="imageapi")

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
            print("PostgreSQL connection is closed")
