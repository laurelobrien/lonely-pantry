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
    email_string = ""
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
    for item in set(grocery_list):
        if item not in stock: # checking stock list in ingredients file
            email_string += item.capitalize() + '\n'
    """print "\nItems excluded because you already have them at home:"
    for item in set(grocery_list):
        if item in stock:
            email_string2 += item.capitalize() + '\n'"""
    return email_string

# enter login credentials and recipient as strings; recipient does not
# have to be a gmail address, but user and pwd does
to = 'recipient@recipient.com'
gmail_user = 'youremail@youraddress.com'
gmail_pwd = 'yourpassword'

# don't need to touch this part!
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Grocery List \n'
print header
msg = header + '\nGrocery List:\
\n\n' + retrieve_ingredients() + '\n\nLove, Laurel'
smtpserver.sendmail(gmail_user, to, msg)
print 'Sent to %s!'%to
smtpserver.close()
