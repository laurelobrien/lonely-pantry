# manual list builder
# turn string input into itemized list

from lonelypantry_ingredients import *

num_meal = int(raw_input("How many meals are you cooking this week? "))

def retrieve_ingredients():
    meal_plan= []
    for count in range(num_meal):
        meal_plan.append(raw_input("Enter meal: "))
    for item in meal_plan:
        print ', '.join(dinner_dict[item])

retrieve_ingredients()

