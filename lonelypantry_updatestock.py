# pantry stock
# fix incorrect loop staging in update_needstock()

import sys
from lonelypantry_ingredients import stock

print "Enter the food items you already have, separated by commas.\n"

def pantry_havestock():
    stock = []
    f = open('lonelypantry_ingredients.py', 'a')
    inventory = raw_input("Item(s) already stocked: ")
    stock.append(inventory.split(', '))
    f.write(str(stock))
    print "Writing to file..."
    f.close()
    print "Closed file."

print "Enter the food items you've run out of since the last stock update,\
 separated by commas.\n"

def pantry_needstock():
    needstock = []
    missing = raw_input("Item(s) you ran out of: ")
    needstock.append(missing.split(', '))
    return needstock

def update_needstock():
    f = open('lonelypantry_ingredients.py', 'w')
    for item in stock:
        if item in pantry_needstock():
            f.write(stock.remove(item))
    print "Deleted items from stock."
    f.close()
    print "Closed file."

update_needstock()
