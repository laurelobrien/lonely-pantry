# pantry stock

import sys

print "Enter the food items you already have, separated by commas.\n"

def pantry_stock():
    stock = []
    f = open('lonelypantry_ingredients.py', 'a')
    inventory = raw_input("Item already stocked: ")
    stock.append(inventory.split(', '))
    f.write(str(stock))
    print "Writing to file..."
    f.close()
    print "Closed file."

pantry_stock()

