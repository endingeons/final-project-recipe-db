from insertDataSqlDb import *
from connectToSqlDb import *
from formatJsonData import *
import pandas as pd
import json

# Main script to read all json files and insert them into the database

PATH_TO_EDAMAM_JSON = '..\\extractData\\edamam-extract\\data\\data.json'
PATH_TO_SPOON_JSON = '..\\extractData\\spoonacular-extract\\data\\data.json'

# Read from JSON
f = open(PATH_TO_EDAMAM_JSON, "rb")
jsonObjectEdamam = json.load(f)
f.close()
edamam_df = parseEdamam(jsonObjectEdamam)

f = open(PATH_TO_SPOON_JSON, "rb")
jsonObjectSpoon = json.load(f)
f.close()
spoon_df = parseSpoonacular(jsonObjectSpoon)

# Connect to SQL Database
# connection = connect_aws_sql_db()
connection = connect_local_sql_db()

# Create database if it doesn't exist
executeScriptsFromFile(connection, '..\\loadData\\create_recipe_db.sql')

# Insert Data
insert_data_from_json(connection, edamam_df)
insert_data_from_json(connection, spoon_df)

# Create Users
create_sample_users(connection)

# Close connection
# close_aws_sql_db(connection)
close_local_sql_db(connection)