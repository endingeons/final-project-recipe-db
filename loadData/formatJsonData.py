def parseEdamam(jsonData):
    # Returns list of tuples, where elements in tuples are dictionaries
    recipe_keys = {'url', 'title', 'serving_size', 'category', 'total_time_minutes',
                   'vegetarian', 'vegan', 'pescatarian', 'vegan', 'gluten_free',
                   'dairy_free', 'peanut_free', 'fats', 'saturated_fats', 'protein', 'cholesterol',
                   'sugar', 'sodium'}

    ingredient_keys = {'ingredient_name', 'category', 'price', 'amount', 'unit'}

    recipe_dict = {key: None for key in recipe_keys}
    ingredient_dict = {key: None for key in ingredient_keys}

    recipes_list = []
    
    for data in jsonData:
        recipe_dict = {'url': data['url']['0'],
                       'title': data['title']['0'],
                       'serving_size': 0, # TODO is this empty?
                       'category': data['category']['0'],
                       'total_time_minutes': data['total_time_minutes']['0'],
                       'vegetarian': data['vegetarian']['0'],
                       'vegan': data['vegan']['0'],
                       'pescatarian': data['pescatarian']['0'],
                       'vegan': data['vegan']['0'],
                       'gluten_free': data['gluten_free']['0'],
                       'dairy_free': data['dairy_free']['0'],
                       'peanut_free': data['peanut_free']['0'],
                       'fats': data['fat']['0'],
                       'saturated_fats': data['satFat']['0'],
                       'protein': data['protein']['0'],
                       'cholesterol': 0, # TODO is this empty?
                       'sugar': data['sugar']['0'],
                       'sodium': data['sodium']['0']}

        ingredientInformation = data['ingredientInformation']['0'][0]
        ingredientList = data['ingredientList']['0'][0]
    
        ingredient_dict = {'ingredient_name': ingredientInformation['name'],
                           'category': ingredientInformation['category'],
                           'price': ingredientInformation['price'],
                           'amount': ingredientList['value'],
                           'unit': ingredientList['unit']}

        # TODO populate ingredient price from Spoonacular

        recipes_list = recipes_list + [(recipe_dict, ingredient_dict)]

    return recipes_list

def parseSpoonacular(jsonData):
    recipes_list = []

    for data in jsonData:
        nutrients = data['nutrition']['nutrients']

        recipe_dict = {'url': data['spoonacularSourceUrl'],
                       'title': data['title'],
                       'serving_size': data['servings'],
                       'category': data['cuisines'],
                       'total_time_minutes': data['readyInMinutes'],
                       'vegetarian': data['vegetarian'],
                       'vegan': data['vegan'],
                       'pescatarian': 'UNKNOWN',
                       'vegan': data['vegan'],
                       'gluten_free': data['glutenFree'],
                       'dairy_free': data['dairyFree'],
                       'peanut_free': 'UNKNOWN',
                       'fats': nutrients['Fat']['percentOfDailyNeeds'],
                       'saturated_fats': nutrients['Saturated Fat']['percentOfDailyNeeds'],
                       'protein': nutrients['Protein']['percentOfDailyNeeds'],
                       'cholesterol': nutrients['Cholesterol']['percentOfDailyNeeds'],
                       'sugar': nutrients['Sugar']['percentOfDailyNeeds'],
                       'sodium': nutrients['Sodium']['percentOfDailyNeeds']}

        ingredientInformation = data['extendedIngredients']

        ingredient_dict = {'ingredient_name': [x['name'] for x in ingredientInformation],
                           'category': [x['aisle'] for x in ingredientInformation],
                           'price': -1,
                           'amount': [x['amount'] for x in ingredientInformation],
                           'unit': [x['unit'] if x['unit'] else 'UNKNOWN' for x in ingredientInformation]}

    recipes_list = recipes_list + [(recipe_dict, ingredient_dict)]

    return recipes_list