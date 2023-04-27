from py_edamam import PyEdamam
from secretKeys import appId, appKey
import pandas as pd

e = PyEdamam(recipes_appid=appId,
           recipes_appkey=appKey)

# Test Loop through data to get information from a single recipe.
def getFoodInfo(search, df_recipeBook, ingredientNum):
  for recipe in e.search_recipe(search):
    df_recipe =  pd.DataFrame()
    print(recipe)
    
    ingredientNum = ingredientNum + 1
    website = recipe.url
    image = recipe.image
    recipeTitle = recipe.label
    servingSize = -1
    foodGenre = recipe.cuisineType
    calories = recipe.calories
    time = recipe.totalTime

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

    # dietary restriciton toggles
    dietaryRestrictions = recipe.healthLabels

    isVegan = False
    isVegetarian = False
    isPescatarian = False
    isDairyFree = False
    isGlutenFree = False
    isPeanutFree = False

    for restrict in dietaryRestrictions:
      if restrict == 'Vegan':
        isVegan = True
      elif restrict == 'Vegetarian':
        isVegetarian = True
      elif restrict == 'Pescatarian':
        isPescatarian = True
      elif restrict == 'Dairy-Free':
        isDairyFree = True
      elif restrict == 'Gluten-Free':
        isGlutenFree = True
      elif restrict == 'Peanut-Free':
        isPeanutFree = True

    ingredientNames = recipe.ingredient_names
    ingredientQuantities = recipe.ingredient_quantities
    
    df_recipe['ingredientNum'] = ingredientNum
    df_recipe['recipeTitle'] = recipeTitle
    df_recipe['recipeSearch_Used'] = search
    df_recipe['website'] = website
    df_recipe['image'] = image
    df_recipe['servingSize'] = servingSize
    df_recipe['foodGenre'] = foodGenre
    df_recipe['calories'] = calories
    df_recipe['time'] = time

    df_recipe['fat'] = fat
    df_recipe['satFat'] = satFat
    df_recipe['protein'] = protein
    df_recipe['cholesterol'] = cholesterol
    df_recipe['sodium'] = sodium
    df_recipe['carbs'] = carbs
    df_recipe['sugar'] = sugar

    df_recipe['isVegan'] = isVegan
    df_recipe['isVegetarian'] = isVegetarian
    df_recipe['isPescatarian'] = isPescatarian
    df_recipe['isDairyFree'] = isDairyFree
    df_recipe['isGlutenFree'] = isGlutenFree
    df_recipe['isPeanutFree'] = isPeanutFree
  
    df_recipe['ingredientNames'] = [ingredientNames]
    df_recipe['ingredientQuantities'] = [ingredientQuantities]
  
    df_recipeBook = df_recipeBook.append(df_recipe)
  
  return df_recipeBook, ingredientNum


# list of foods
PATH = "C:\\Users\\PC\\code\\githubProjects\\final-project-recipe-db\\"
listOfFoods = ['Chicken Parmesan', 'Cheeseburger', 'Ham', 'Scrambled Eggs', 'Egg Sandwich', 'Bread', 'Pizza', 'Pasta', 'Sweet Tea']
df =  pd.DataFrame()

# used a large number so i dont overlap with Chelsea
ingredientNum = 10000

for food in listOfFoods:
  df, ingredientNum = getFoodInfo(food, df, ingredientNum)
  print('Search Complete: ' + food)
  print(ingredientNum)
  print()

df.to_csv(PATH, index=False)

# for testing purposes
  #print(recipe.url)
  #print('\n')
  #print(recipe.cuisineType)
  #print(recipe.calories)
  #for i in recipe.ingredient_names:
  #    print(i)
  #print('\n')
  #print(recipe.ingredient_quantities)

'''Recipies
Recipy Key
   URL              ---
   Recipe Title     ---
   Serving Size
   Food Genre       ---
   Calories         ---
   Time             ---

Users
   User key
   Recipy Key
   Dietary Restrictions ---

Ingredient List
   Recipe Key 
   Ingredient Key
   value
   Unit

Recipy Nutrition
   Recipy Key
   Fats              ---
   Saturated Fats    ---
   Protein           ---
   Cholesterol       ---
   Sugar 
   Sodium            ---
   Vitamins

Ingredient Info
    Name
    Category
    Price


'''
# OLD NOTES
# what to have in database 
# Ingredients (name)

# general
# quanity
# url?
# food genre (Italian, Mexican, Inian, etc)
# serving size (amount of people you can feed)
# calories
# time

# nutrition  facts
# fats
# cholesteral
# sugar