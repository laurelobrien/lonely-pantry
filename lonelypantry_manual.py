# manual list builder
# TODO: turn string input into itemized list, remove duplicates in grocery list

from lonelypantry_ingredients import *

def retrieve_ingredients():
    num_meal = int(raw_input("How many meals are you cooking this week? "))
    additionals = raw_input("Enter any essentials separated by commas, such \
as coffee cream or toilet paper.\nIf there are none needed, press n. ")
    print "Meals for the week - hit enter after each meal."
    meal_plan = []
    grocery_list = []
    for count in range(num_meal):
        meal_plan.append(raw_input("Enter meal: "))
    meal_plan = set(meal_plan) #eliminates duplicates
    for item in meal_plan:
        grocery_list.extend(dinner_dict[item]) #merges ingredient lists
    if additionals != 'n':
        grocery_list.extend(additionals.split(', '))
    print "\nGrocery List\n"
    for item in set(grocery_list):
        if item not in stock: # checking stock list in ingredients file
            print item.capitalize()
    print "\nItems excluded because you already have them at home:"
    for item in set(grocery_list):
        if item in stock:
            print item.capitalize()

retrieve_ingredients()

