# manual list builder
# to do: account for user typos and ask for a new entry
# to do: divide entire script into neater functions?

from lonelypantry_ingredients import *
import smtplib

def retrieve_ingredients():
    num_meal = int(raw_input("How many meals are you cooking this week? "))
    additionals = raw_input("Enter any essentials separated by commas, such \
as coffee cream or toilet paper.\nIf there are none needed, press 'n'. ")
    print "Meals for the week - hit enter after each meal."
    meal_plan = []
    grocery_list = []
    for count in range(num_meal):
        meal_plan.append(raw_input("Enter meal: ").lower())
    meal_plan = set(meal_plan) #eliminates duplicates
    for item in meal_plan:
        grocery_list.extend(dinner_dict[item]) #merges ingredient lists
    if additionals != 'n':
        grocery_list.extend(additionals.split(', '))
    # printing final grocery list
    print "\nGrocery List\n"
    for item in set(grocery_list):
        if item not in stock: # checking stock list in ingredients file
            print item.capitalize()
    print "\nItems excluded because you already have them at home:"
    for item in set(grocery_list):
        if item in stock:
            print item.capitalize()

# enter login credentials and recipient as strings; recipient does not
# have to be a gmail address, but user and pwd does
to = 'placeholder@placeholder.com'
gmail_user = 'filler@filler.com'
gmail_pwd = 'yourpassword'

# don't need to touch this part!
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print header
msg = header + '\n optional email-body text here \n\n' + str(
    retrieve_ingredients())
smtpserver.sendmail(gmail_user, to, msg)
print 'Sent!'
smtpserver.close()
