# manual list builder
# TODO: turn string input into itemized list, remove duplicates in grocery list

import itertools
from lonelypantry_ingredients import *


num_meal = int(raw_input("How many meals are you cooking this week? "))

def retrieve_ingredients():
    meal_plan = []
    grocery_list = []
    for count in range(num_meal):
        meal_plan.append(raw_input("Enter meal: "))
    meal_plan = set(meal_plan)
    for item in meal_plan:
        grocery_list.append(dinner_dict[item])
        #itertools.chain(grocery_list)
    print grocery_list

retrieve_ingredients()

