# recipe input

meal = []
recipe = raw_input("Recipe name: ")
recipe_mats = raw_input("Ingredients, separated by commas: ")
meal.append(recipe.upper())
meal.append(recipe_mats.split(', '))

print meal

"""f = open('lonelypantry_ingredients', 'a')
f.append(meal"""
