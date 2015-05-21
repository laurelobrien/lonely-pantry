# TODO // remove duplicates, make tool for recipe input, email list

# lonely pantry tool
import random
from lonelypantry_ingredients import *

# interpretation
dinnerlist = ['fried rice', 'stir fried noodles', 'hot and sour soup', 'pizza', 'eggs benedict', 'sushi bowl', 'grilled cheese', 'teriyaki chicken', 'sautee salmon', 'ramen', 'pasta cabonara', 'gnocchi', 'carnitas tacos', 'quesadillas']
breakfastlist = ['eggs benedict','cinnamon buns','iced coffee','smoothie','cereal']

# user input
dinners = int(raw_input('How many dinners are you cooking this week? '))
#breakfasts = int(raw_input('And how many breakfasts? '))

#determine how many meals to print
def mealplan():
        meal_list = []
        for meals in range(dinners):
                meal_list.append(random.choice(dinnerlist))
        return meal_list
        
def print_plan():
        print 'Meal Plan:'
        for i in mealplan():
                i = str(i).capitalize()
                print i

def buildlist():
        confirm = raw_input('Does this sound like a good meal plan? y/n: ')
        grocery_list = []
        if confirm in 'y':
                print 'Grocery list:'
                for i in mealplan():
                        if i not in grocery_list:
                                grocery_list.append(dinner_dict[i])
        elif confirm in 'n':
                        print 'tough shit' #placeholder for meal replacement
        else:
                print 'You had one job.' #placeholder for user re-input
        for item in grocery_list:
                print ', '.join(item)

print_plan()
buildlist()

