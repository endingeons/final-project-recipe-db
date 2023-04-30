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

def parseSpoonacular(data):
    print('this doesn''t do anything yet')
    return []