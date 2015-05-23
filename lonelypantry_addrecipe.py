# recipe input

meal = []
recipe = raw_input("Recipe name: ")
recipe_mats = raw_input("Ingredients, separated by commas: ")

# format string to resemble a list definition
recipe = recipe.replace(' ','_')
meal.append(recipe+' =')
meal.append(recipe_mats.split(', '))

print "Added %s to lonelypantry_ingredients."%(recipe.replace('_',' ')
                                                 .capitalize())
f = open('lonelypantry_ingredients.py', 'a')
f.write(str(meal))
f.close()
