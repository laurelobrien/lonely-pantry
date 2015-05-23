# TODO // remove duplicates in meal plan
# make tool for recipe input, email list

# lonely pantry tool
import random
from lonelypantry_ingredients import *

# interpretation
dinnerlist = ['fried rice', 'stir fried noodles', 'hot and sour soup', 'pizza',
              'eggs benedict', 'sushi bowl', 'grilled cheese',
              'teriyaki chicken','sautee salmon', 'ramen', 'pasta cabonara',
              'gnocchi', 'carnitas tacos', 'quesadillas']
breakfastlist = ['eggs benedict','cinnamon buns','iced coffee','smoothie',
                 'cereal']

# user input
dinners = int(raw_input('How many dinners are you cooking this week? '))
#breakfasts = int(raw_input('And how many breakfasts? '))

#determine how many meals to print
def mealplan():
        meal_list = []
        while len(meal_list) <= dinners-1:
                random_meal = random.choice(dinnerlist)
                if random_meal not in meal_list:
                        meal_list.append(random_meal)
        return meal_list
        
def print_plan():
        print '\nMeal Plan\n'
        for i in mealplan():
                i = str(i).capitalize()
                print i

# generate shopping list out of meal plan,
#or re-generate a more acceptable one
def buildlist():
        confirm = raw_input('Does this sound like a good meal plan? y/n: ')
        grocery_list = []
        if confirm in 'y':
                print '\nGrocery list\n'
                for i in mealplan():
                        grocery_list.extend(dinner_dict[i])
        elif confirm in 'n':
                        print 'tough shit' #placeholder for meal replacement
        else:
                print 'You had one job.' #placeholder for user re-input
        for item in set(grocery_list):
                print item.capitalize()

print_plan()
buildlist()

