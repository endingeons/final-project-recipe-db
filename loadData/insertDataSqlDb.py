import mysql.connector
from mysql.connector import Error
import pandas as pd

def insert_data_from_json(connection, data):
    print('Starting to insert data into SQL db')
    # Start adding recipes, going one by one through list of tuples
    # Looks like := [tuple, tuple, tuple]
    # Each tuple is := (recipe_dict, ingredient_dict)
    for d in data:
        r = d[0]
        ingredient_list_vals = []

        print(r['title'])

        if r['pescatarian'] == 'UNKNOWN':
            r['pescatarian'] = -1
        if r['peanut_free'] == 'UNKNOWN':
            r['peanut_free'] = -1

        # recipe_key(AUTO), url, title, serving_size, category, total_time_minutes,
        # vegetarian, pescatarian, vegan, gluten_free, dairy_free, peanut_free
        recipe_vals = [(r['url'], r['title'], r['serving_size'],
                        r['category'][0], r['total_time_minutes'],
                        r['vegetarian'], r['pescatarian'], r['vegan'], r['gluten_free'],
                        r['dairy_free'], r['peanut_free'])]

        curr_recipe_id = execute_list_query(connection, pop_recipes(), recipe_vals)
        curr_recipe_id = curr_recipe_id[0][0]
        # recipe_nutrition_key(AUTO), recipe_key, fats, saturated_fats, protein, cholesterol, sugar, sodium
        recipe_nutrition_vals = [(curr_recipe_id, r['fats'], r['saturated_fats'],
                                  r['protein'], r['cholesterol'], r['sugar'], r['sodium'])]
        execute_list_query(connection, pop_recipe_nutrition(), recipe_nutrition_vals)

        ingredients = d[1]
        num_ingredients = len(ingredients['ingredient_name'])
        for idx in range(0, num_ingredients):
            i = {k: v[idx] for (k, v) in ingredients.items()}
            
            if i['category'] == None:
                i['category'] = 'none'
            
            if i['unit'] == None:
                i['unit'] = 'none'

            # ingredient_key(AUTO), ingredient_name, category
            ingredient_information_vals = [(i['ingredient_name'], i['category'])]

            curr_ingredient_id = execute_list_query(connection, pop_ingredient_information(),
                                                    ingredient_information_vals)
            curr_ingredient_id = curr_ingredient_id[0][0]
          
            ingredient_list_vals = ingredient_list_vals + [(curr_recipe_id, curr_ingredient_id,
                                                            i['amount'], i['unit'])]

        # list_key(AUTO), recipe_key, ingredient_key, amount, unit
        execute_list_query(connection, pop_ingredient_list(), ingredient_list_vals)

    print('Done!')

def create_sample_users(connection):
    user_vals = [(True, False, False, True, False, False),
                 (False, False, False, True, False, False),
                 (True, False, False, False, False, False),
                 (False, False, False, False, False, False)]
    execute_list_query(connection, pop_users(), user_vals)

    user_fav_recipe_vals = [(1, 1), (1, 2), (1, 3), (2, 3), (2, 30),
                            (3, 5), (4, 10), (4, 11)]

    execute_list_query(connection, pop_users_fav_recipes(), user_fav_recipe_vals)

def pop_users_fav_recipes():
    sql = """
            INSERT INTO users_fav_recipes (user_key, recipe_key)
            VALUES (%s, %s)
        """
    return sql

def pop_users():
    sql = """
        INSERT INTO users (vegetarian, pescatarian, vegan, gluten_free, dairy_free, peanut_free)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    return sql

def pop_recipe_nutrition():
    sql = """
        INSERT INTO recipe_nutrition (recipe_key, fats, saturated_fats, protein, cholesterol, sugar, sodium)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    return sql

def pop_recipes():
    sql = """
            INSERT INTO recipes (url, title, serving_size, category, total_time_minutes, 
                                 vegetarian, pescatarian, vegan, gluten_free, dairy_free, peanut_free)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
    return sql

def pop_ingredient_list():
    sql = """
            INSERT INTO ingredient_list (recipe_key, ingredient_key, amount, unit)
            VALUES (%s, %s, %s, %s)
        """
    return sql

def pop_ingredient_information():
    sql = """
            INSERT INTO ingredient_information (ingredient_name, category)
            VALUES (%s, %s)
        """
    return sql

def execute_query(connection, query):
    # https://www.freecodecamp.org/news/connect-python-with-sql/
    cursor = connection.cursor()
    try:
        cursor.execute('USE recipe')
        cursor.execute(query)
        connection.commit()
        # print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def execute_list_query(connection, sql, val):
    # https://www.freecodecamp.org/news/connect-python-with-sql/
    cursor = connection.cursor()
    try:
        cursor.execute('USE recipe')
        cursor.executemany(sql, val)
        connection.commit()
        cursor.execute('SELECT LAST_INSERT_ID()')
        # print("Query successful")
        return cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}'")

def executeScriptsFromFile(connection, filename):
    cursor = connection.cursor()

    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        
        command = command.replace("\n", '')
        command = command.replace("\t", ' ')

        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            cursor.execute(command)
        except Error as err:
            print(f"Error: '{err}'")
