import mysql.connector
from mysql.connector import Error
import pandas as pd
from getAPIDataJson import *

def insert_data_from_json(connection, jsonData, apiFormat):
    if apiFormat == 'edamam':
        # Blank
    elif apiFormat == 'spoonacular':
        # Blank
    else:
        print('Incorrect API Format Provided.')
        return -1

def pop_recipe_nutrition():
    sql = """
        INSERT INTO recipe_nutrition (recipe_nutrition_key, recipe_key, fats, saturated_Fats, protein, cholesterol, sugar, sodium)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    return sql

def pop_recipes():
    sql = """
            INSERT INTO recipes (recipe_key, url, title, serving_size, category, total_time)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
    return sql

def pop_ingredient_list():
    sql = """
            INSERT INTO ingredient_list (list_key, recipe_key, ingredient_key, amount, unit)
            VALUES (%s, %s, %s, %s, %s)
        """
    return sql

def pop_ingredient_information():
    sql = """
            INSERT INTO ingredient_information (ingredient_key, ingredient_name, category, price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
    return sql



def execute_query(connection, query):
    # https://www.freecodecamp.org/news/connect-python-with-sql/
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def execute_list_query(connection, sql, val):
    # https://www.freecodecamp.org/news/connect-python-with-sql/
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")