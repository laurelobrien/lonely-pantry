# manual list builder
# turn string input into itemized list

from lonelypantry_ingredients import *

meal_plan = raw_input("What would you like to cook this week? Separate\
                      with commas. ")

def retrieve_ingredients():
    for item in meal_plan:
        print dinner_dict[item]

