from loadData.insertDataSqlDb import *
from loadData.connectToSqlDb import *

# Connect
connection = connect_local_sql_db()

# Create
with open('create_recipe_db.sql', 'r') as sql_file:
    connection.executescript(sql_file.read())

# Insert some data
val = [(), ()]
# ingredient_key, ingredient_name, category, price
execute_list_query(connection, pop_ingredient_information, val)

val = []
# list_key, recipe_key, ingredient_key, amount, unit
execute_list_query(connection, pop_ingredient_list, val)

val = []
# recipe_key, url, title, serving_size, category, total_time
execute_list_query(connection, pop_recipes, val)

val = []
# recipe_nutrition_key, recipe_key, fats, saturated_Fats, protein, cholesterol, sugar, sodium
execute_list_query(connection, pop_recipe_nutrition, val)


# Close connection?