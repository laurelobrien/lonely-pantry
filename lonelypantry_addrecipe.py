# recipe input

import sys
    
def format_input():
    meal = []
    recipe = raw_input("Recipe name: ")
    recipe_mats = raw_input("Ingredients, separated by commas: ")
    recipe = recipe.replace(' ','_')
    meal.append(recipe+' =')
    meal.append(recipe_mats.split(', '))
    return meal

# append string (imitating list) to ingredients file
def write_new():
    f = open('lonelypantry_ingredients.py', 'a')
    f.write('\n'+str(format_input()))
    f.close()
    print "Recipe added to lonelypantry_ingredients.py successfully."
    add_another()

def add_another():
    repeat = raw_input("Add another? y / n: ")
    if repeat == 'y':
        write_new()
    elif repeat == 'n':
        sys.exit()
    else:
        print "Sorry, I didn't understand you. Please press y or n followed by enter."
        add_another()

write_new()

    
    


