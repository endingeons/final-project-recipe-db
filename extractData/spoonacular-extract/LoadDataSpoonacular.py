from spoonacularAPIKeys import api_key
import spoonacular as sp
import json
import re
import time

PATH_TO_SPOON_JSON = 'data\\data.json'
NUMBER_OF_RECIPES = 100
p = re.compile(r'[\d]+$')
allRecipes = []

# Connect to API
api = sp.API(api_key)

response = api.get_random_recipes(number=NUMBER_OF_RECIPES)
random_recipes = response.json()

for recipe in random_recipes['recipes']:
    try:
        recipe_id = p.search(recipe['spoonacularSourceUrl']).group()
        response_recipe = api.get_recipe_information(id=recipe_id, includeNutrition=True)
        x = response_recipe.json()
        allRecipes.append(x)

    except:
        print('Failed to get recipe, continuing to next one')
        time.sleep(5)
        continue

    time.sleep(2)

data = {'recipes': allRecipes}

# Write JSON file
with open(PATH_TO_SPOON_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
