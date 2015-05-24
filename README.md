# Lonely-Pantry
Lonely Pantry is a beginner python project for building a grocery list out of desired meals and essential items.
You can either generate a randomized meal plan if you're not feeling fussy, or enter your own meals for the week.

A basic read/write function allows you to add recipes to your recipe book (lonelypantry_ingredients.py) with less 
fuss than entering a list manually, although it still requires some formatting after it's been appended to 
the ingredients file, and still needs a dictionary entry so python can fetch the list of ingredients associated
with the user's string entry (eg, {'fried rice':fried_rice}, and fried_rice is a list of ingredients.)

The stock[] list in the recipe book contains items you already have at home, so you don't need to buy them twice. ;)
Lonely Pantry will exclude them from your final shopping list.

To-Dos include finding a more efficient way to add recipes and stocked items to _ingredients.py, coding for more
possible user errors (such as misspellings), and emailing an accepted grocery list to the user so they can take it
with them to the store. End goal is a GUI so you don't need to be a python baby to make use of it, and can enter
your own recipes without digging around in .py files.
