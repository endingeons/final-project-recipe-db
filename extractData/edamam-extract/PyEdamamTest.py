from py_edamam import PyEdamam
from secretKeys import appId, appKey
#import pandas as pd

import json
import time as t

e = PyEdamam(recipes_appid=appId,
           recipes_appkey=appKey)

# Test Loop through data to get information from a single recipe.
def getFoodInfo(search, df_recipe, recipeKey, ingredientKey):
  for recipe in e.search_recipe(search):
    #print(recipe)  
    
    recipeKey = recipeKey + 1
    website = recipe.url
    image = recipe.image
    recipeTitle = recipe.label
    #servingSize = -1
    category = recipe.cuisineType
    calories = recipe.calories
    total_time_minutes = recipe.totalTime

    fat =  recipe.digest['Fat']['daily']
    protein =  recipe.digest['Protein']['daily']
    cholesterol =  recipe.digest['Cholesterol']['daily']
    sodium =  recipe.digest['Sodium']['daily']
    carbs =  recipe.digest['Carbs']['daily']
   
    parseInfo = recipe.totalDaily
    # obtain the saturated fat percentage
    if parseInfo[2].label == 'Saturated':
      satFat = parseInfo[2].quantity
    else:
      satFat = -1
      for num in parseInfo:
        if num.label == 'Saturated':
          satFat = num.quantity
          break
    
    parseInfo = recipe.totalNutrients
    # obtain the sugar percentage
    if parseInfo[9].label == 'Sugars':
      sugar = parseInfo[2].quantity
    else:
      sugar = -1
      for num in parseInfo:
        if num.label == 'Sugars':
          sugar = num.quantity
          break

    # dietary restriction toggles
    dietaryRestrictions = recipe.healthLabels

    vegan = False
    vegetarian = False
    pescatarian = False
    dairy_free = False
    gluten_free = False
    peanut_free = False

    for restrict in dietaryRestrictions:
      if restrict == 'Vegan':
        vegan = True
      elif restrict == 'Vegetarian':
        vegetarian = True
      elif restrict == 'Pescatarian':
        pescatarian = True
      elif restrict == 'Dairy-Free':
        dairy_free = True
      elif restrict == 'Gluten-Free':
        gluten_free = True
      elif restrict == 'Peanut-Free':
        peanut_free = True

    ingredientQuantities = recipe.ingredient_quantities

    # populate dictionary
    df_recipe['recipe_key'].append(recipeKey)
    df_recipe['title'].append(recipeTitle)
    df_recipe['recipeSearch_Used'].append(search)
    df_recipe['url'].append(website)
    df_recipe['image'].append(image)
    #df_recipe['servingSize'].append(servingSize)
    df_recipe['category'].append(category)
    df_recipe['calories'].append(calories)
    df_recipe['total_time_minutes'].append(total_time_minutes)

    df_recipe['fat'].append(fat)
    df_recipe['satFat'].append(satFat)
    df_recipe['protein'].append(protein)
    df_recipe['cholesterol'].append(cholesterol)
    df_recipe['sodium'].append(sodium)
    df_recipe['carbs'].append(carbs)
    df_recipe['sugar'].append(sugar)

    df_recipe['vegan'].append(vegan)
    df_recipe['vegetarian'].append(vegetarian)
    df_recipe['pescatarian'].append(pescatarian)
    df_recipe['dairy_free'].append(dairy_free)
    df_recipe['gluten_free'].append(gluten_free)
    df_recipe['peanut_free'].append(peanut_free)
    
    ingredientList = {'recipe_key':[],
                  'ingredient_key':[],
                  'value': [],
                  'unit':[]}

    ingredientInformation = {'ingredient_key':[],
                          'name':[],
                          'category':[],
                          'price':[]}

    for idx, ingredient in enumerate(ingredientQuantities):
      ingredientList['recipe_key'].append(recipeKey)
      ingredientList['ingredient_key'].append(ingredientKey)
      ingredientList['value'].append(ingredient['quantity'])
      ingredientList['unit'].append(ingredient['measure'])
      
      ingredientInformation['ingredient_key'].append(ingredientKey)
      ingredientInformation['name'].append(filterRecipe(ingredient['text']))
      ingredientInformation['category'].append(ingredient['foodCategory'])
      ingredientInformation['price'].append(-1)

      ingredientKey = ingredientKey + 1

    df_recipe['ingredientList'].append([ingredientList])
    df_recipe['ingredientInformation'].append([ingredientInformation])
   
    # df_recipe = pd.DataFrame(df_recipe)
    # df_recipe.to_csv("C:\\Users\\PC\\code\\githubProjects\\final-project-recipe-db\\testing1.csv", index=False)
    
    #df_recipeBook = df_recipeBook.append(df_recipe)

  return df_recipe, recipeKey

def filterRecipe(text):
  remove_list = ['½', '¼', '¾', '1','2','3','4','5','6','7','8','9','0', 'ml', 'teaspoon', 'teaspoons', 
                 '/', 'tablespoon', 'tablespoons', 'cup', '-', 'Tbsp', 'tbsp', 'ounce', 'ounces', '\\u00bd',
                 'pound', '\\u00be', '\\u00bc', 'lb.', 'lb', 'tsp.', 'tsp', 'tbsp.', 'slices', 'handful', 'oz', 
                 'oz.', ' s ', ' g ', '(', ')', '*', '+', '.', '–', ' x ', '%', 'inch', 'cm']

  for delete in remove_list:
    if delete in text:
      text = text.replace(delete, '')

  while text[0] == " ":
    text = text[1:len(text)]
  
  return text

''' old filter code
  # find whitespace
  for idx, letter in enumerate(text):
    if letter == ' ':
      whitespace.append(idx)
  
  for idx, nothing in enumerate(whitespace):
    # use for end
    if idx == len(whitespace)-1:
      if not text[whitespace[idx]:len(text)] in remove:
        new_text = new_text + text[whitespace[idx]:len(text)]
      break

    # use for beginning
    if idx == 0 and not text[0:whitespace[idx]] in remove:
      new_text = text[0:whitespace[idx]]

    # use for middle
    if not text[whitespace[idx]+1:whitespace[idx+1]] in remove:
      new_text = new_text + text[whitespace[idx]+1:whitespace[idx+1]]

  if new_text[0] == " ":
    new_text = new_text[1:len(text)]
  '''

# list of foods
PATH = "C:\\Users\\PC\\code\\githubProjects\\final-project-recipe-db\\data.csv"
listOfFoods = ['Tacos', 'Chicken Parmesan', 'Cheeseburger', 'Ham', 'Scrambled Eggs', 'Egg Sandwich', 'Bread', 'Pizza', 'Pasta', 'Sweet Tea', 'Nacho']
#df = pd.DataFrame()
df = []

# used a large number so i dont overlap with Chelsea
recipeKey = 10000
ingredientKey = 10000

# make a dictionary
df_recipe = {'recipe_key':[],
              'title':[],
              'recipeSearch_Used':[],
              'url':[],
              'image':[],
              #'servingSize':[],
              'category':[],
              'calories':[],
              'total_time_minutes':[],

              'fat':[],
              'satFat':[],
              'protein':[],
              'cholesterol':[], 
              'sodium':[],
              'carbs':[],
              'sugar':[],
              
              'vegan':[],
              'vegetarian':[],
              'pescatarian':[],
              'dairy_free':[],
              'gluten_free':[],
              'peanut_free':[],
              
              'ingredientList':[],
              'ingredientInformation':[]}

for food in listOfFoods:
  df_recipe, recipeKey = getFoodInfo(food, df_recipe, recipeKey, ingredientKey)
  print('Search Complete: ' + food)
  print(recipeKey)

  # used to not overwhelm server
  t.sleep(5)
  print()

#df.to_csv(PATH, index=False)
#df.to_dict() 

with open("C:\\Users\\PC\\code\\githubProjects\\final-project-recipe-db\\data.json", "w") as write_file:
  json.dump(df_recipe, write_file, indent=4)