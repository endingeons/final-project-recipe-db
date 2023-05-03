def parseEdamam(jsonData):
    print('Trying to parse JSON file of Edamam data')
    # Returns list of tuples, where elements in tuples are dictionaries

    recipes_list = []
    numRecipes = len(jsonData['title'])
    for idx in range(0, numRecipes):
        recipe_dict = {'url': jsonData['url'][idx],
                       'title': jsonData['title'][idx],
                       'serving_size': 0, # TODO is this empty?
                       'category': jsonData['category'][idx],
                       'total_time_minutes': jsonData['total_time_minutes'][idx],
                       'vegetarian': jsonData['vegetarian'][idx],
                       'vegan': jsonData['vegan'][idx],
                       'pescatarian': jsonData['pescatarian'][idx],
                       'vegan': jsonData['vegan'][idx],
                       'gluten_free': jsonData['gluten_free'][idx],
                       'dairy_free': jsonData['dairy_free'][idx],
                       'peanut_free': jsonData['peanut_free'][idx],
                       'fats': jsonData['fat'][idx],
                       'saturated_fats': jsonData['satFat'][idx],
                       'protein': jsonData['protein'][idx],
                       'cholesterol': jsonData['cholesterol'][idx],
                       'sugar': jsonData['sugar'][idx],
                       'sodium': jsonData['sodium'][idx]}

        ingredientInformation = jsonData['ingredientInformation'][idx][0]
        ingredientList = jsonData['ingredientList'][idx][0]
    
        ingredient_dict = {'ingredient_name': ingredientInformation['name'],
                           'category': ingredientInformation['category'],
                           'price': ingredientInformation['price'],
                           'amount': ingredientList['value'],
                           'unit': ingredientList['unit']}

        # TODO populate ingredient price from Spoonacular

        recipes_list = recipes_list + [(recipe_dict, ingredient_dict)]

    print('Done!')
    return recipes_list

def parseSpoonacular(jsonData):
    print('Trying to parse JSON file of Spoonacular data')
    recipes_list = []

    for data in jsonData['recipes']:
        nutrients = data['nutrition']['nutrients']

        recipe_dict = {'url': data['spoonacularSourceUrl'],
                       'title': data['title'],
                       'serving_size': data['servings'],
                       'category': 'None', # TODO: Not populating w/ api for some reason. data['cuisines'],
                       'total_time_minutes': data['readyInMinutes'],
                       'vegetarian': data['vegetarian'],
                       'vegan': data['vegan'],
                       'pescatarian': 'UNKNOWN',
                       'vegan': data['vegan'],
                       'gluten_free': data['glutenFree'],
                       'dairy_free': data['dairyFree'],
                       'peanut_free': 'UNKNOWN',
                       'fats': [x['percentOfDailyNeeds'] for x in nutrients if x['name'] == 'Fat'][0],
                       'saturated_fats': [x['percentOfDailyNeeds'] for x in nutrients if x['name'] == 'Saturated Fat'][0],
                       'protein': [x['percentOfDailyNeeds'] for x in nutrients if x['name'] == 'Protein'][0],
                       'cholesterol': [x['percentOfDailyNeeds'] for x in nutrients if x['name'] == 'Cholesterol'][0],
                       'sugar': [x['percentOfDailyNeeds'] for x in nutrients if x['name'] == 'Sugar'][0],
                       'sodium': [x['percentOfDailyNeeds'] for x in nutrients if x['name'] == 'Sodium'][0]}

        ingredientInformation = data['extendedIngredients']

        ingredient_dict = {'ingredient_name': [x['name'] for x in ingredientInformation],
                           'category': [x['aisle'] for x in ingredientInformation],
                           'price': [-1] * len(ingredientInformation),
                           'amount': [x['amount'] for x in ingredientInformation],
                           'unit': [x['unit'] if x['unit'] else 'UNKNOWN' for x in ingredientInformation]}

        recipes_list = recipes_list + [(recipe_dict, ingredient_dict)]

    print('Done!')
    return recipes_list