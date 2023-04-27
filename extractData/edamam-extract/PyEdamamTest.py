from py_edamam import PyEdamam
from secretKeys import appId, appKey
import pandas as pd

e = PyEdamam(recipes_appid=appId,
           recipes_appkey=appKey)

for recipe in e.search_recipe("Pinapple Ham"):
  print(recipe)
  #print(recipe.calories)
  #print(recipe.cautions, recipe.dietLabels, recipe.healthLabels)
  
  URL = recipe.url
  recipeTitle = recipe
  servingSize = 'nan'
  foodGenre = recipe.cuisineType
  calories = recipe.calories
  time = recipe.totalTime

  #saturated fats
  fat =  recipe.digest['Fat']['total']
  fatU =  recipe.digest['Fat']['unit']
  
  protein =  recipe.digest['Protein']['total']
  protienU =  recipe.digest['Protein']['unit']

  cholesterol =  recipe.digest['Cholesterol']['total']
  cholesterolU =  recipe.digest['Cholesterol']['unit']
  
  sodium =  recipe.digest['Sodium']['total']
  sodiumU =  recipe.digest['Sodium']['unit']

  # Carbs?? might be regular fats?
  carbs =  recipe.digest['Carbs']['total']
  carbsU =  recipe.digest['Carbs']['unit']

  dietaryRestrictions =  recipe.healthLabels

  ingrediantNames = recipe.ingredient_names
  ingrediantQuantities = recipe.ingredient_quantities

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
   Saturated Fats
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