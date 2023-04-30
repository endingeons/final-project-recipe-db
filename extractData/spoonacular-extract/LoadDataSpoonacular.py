from spoonacularAPIKeys import api_key
import spoonacular as sp
import pandas as pd

api = sp.API(api_key)

recipes = {'url', 'title', 'serving_size', 'category', 'total_time_minutes', 'vegetarian',
           'pescatarian', 'vegan', 'gluten_free', 'dairy_free', 'peanut_free', 'fats', 'saturated_fats',
           'protein', 'cholesterol', 'sugar', 'sodium'}
ingredients = {'ingredient_name', 'category', 'price', 'amount', 'unit'}

# Each row in the dataframe is one recipe







# Write JSON file