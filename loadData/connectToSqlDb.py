from localSQLConfig import host_name, user_name, user_password
import mysql.connector
from mysql.connector import Error
import pandas as pd

def connect_local_sql_db():
    # https://www.freecodecamp.org/news/connect-python-with-sql/
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def connect_aws_sql_db(connection):
    # something
    handle = 0
    return handle

def close_local_sql_db(connection):
    connection.close()

def close_aws_sql_db(connection):
    # something 
    print('test')