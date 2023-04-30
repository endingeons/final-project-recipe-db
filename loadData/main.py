from insertDataSqlDb import *
from connectToSqlDb import *
import pandas as pd
import json

# Main script to read all json files and insert them into the database

PATH_TO_EDAMAM_JSON = ''
PATH_TO_SPOON_JSON = ''

# Read from JSON
f = open(PATH_TO_EDAMAM_JSON, "rb")
jsonObjectEdamam = json.load(f)
f.close()

f = open(PATH_TO_SPOON_JSON, "rb")
jsonObjectSpoon = json.load(f)
f.close()

# Connect to SQL Database
# cursor = connect_aws_sql_db()
cursor = connect_local_sql_db()

# Create database if it doesn't exist


# Insert Data
edamam_df = insert_data_from_json(cursor, jsonObjectEdamam, 'edamam')
spoon_df = insert_data_from_json(cursor, jsonObjectSpoon, 'spoonacular')

# Close connection
# close_aws_sql_db(cursor)
close_local_sql_db(cursor)