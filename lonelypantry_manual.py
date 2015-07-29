# manual list builder
# to do: account for user typos and ask for a new entry
# make format_departments() functional for email body text
# to do: use html in email final (header, bold etc)

from lonelypantry_ingredients import *
import smtplib

def retrieve_ingredients():
    num_meal = int(raw_input("How many meals are you cooking this week? "))
    additionals = raw_input("Enter any essentials separated by commas, such \
as coffee cream or toilet paper.\nIf there are none needed, press 'n'. ")
    print "Meals for the week - hit enter after each meal."
    email_string = []
    meal_plan = []
    grocery_list = []
    for count in range(num_meal):
        meal_plan.append(raw_input("Enter meal: ").lower())
    meal_plan = set(meal_plan) #eliminates duplicates
    for item in meal_plan:
        grocery_list.extend(dinner_dict[item]) #merges ingredient lists
    if additionals != 'n':
        grocery_list.extend(additionals.split(', '))
    for item in set(grocery_list):
        if item not in stock: # checking stock list in ingredients file
            email_string.append(item)
    """print "\nItems excluded because you already have them at home:"
    for item in set(grocery_list):
        if item in stock:
            email_string2 += item.capitalize() + '\n'"""
    return email_string

# to do: remove departments from print output which have no ingredients in them
# remove repetitions by creating classes
def format_departments():
    email_produce = ""
    email_household = ""
    email_dairy = ""
    email_meat = ""
    email_baking = ""
    email_starchsauce = ""
    email_frozen = ""
    email_other = ""
    for item in retrieve_ingredients():
        if item in dept_produce:
            email_produce += (item.capitalize() + '\n')
        elif item in dept_household:
            email_household += (item.capitalize() + '\n')
        elif item in dept_dairy:
            email_dairy += item.capitalize() + '\n'
        elif item in dept_meat:
            email_meat += (item.capitalize() + '\n')
        elif item in dept_baking:
            email_baking += (item.capitalize() + '\n')
        elif item in dept_starchsauce:
            email_starchsauce += (item.capitalize() + '\n')
        elif item in dept_frozen:
            email_frozen += (item.capitalize() + '\n')
        else:
            email_other += (item.capitalize() + '\n')
    if email_produce != "":
        print '\n| PRODUCE |'
        print email_produce
    if email_household != "":
        print '\n| HOUSEHOLD |'
        print email_household
    if email_meat != "":
        print '\n| MEAT |'
        print email_meat
    if email_dairy != "":
        print '\n| DAIRY |'
        print email_dairy
    if email_baking != "":
        print '\n| BAKING |'
        print email_baking
    if email_starchsauce != "":
        print '\n| STARCHES & SAUCES |'
        print email_starchsauce
    if email_frozen != "":
        print '\n| FROZEN |'
        print email_frozen
    if email_other != "":
            print '\n| OTHER |'
            print email_other

format_departments()


# format_departments() does not create a value that can be printed into an email yet
'''# enter login credentials and recipient as strings; recipient does not
# have to be a gmail address, but user and pwd does
to = 'recipient@blank.com'
gmail_user = 'yourgmail@gmail.com'
gmail_pwd = 'yourpassword'

# don't need to touch this part!
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Grocery List \n'
print header
msg = header + '\nYour grocery list from Lonely Pantry:\
\n\n' + format_departments()
smtpserver.sendmail(gmail_user, to, msg)
print 'Sent to %s!'%to
smtpserver.close()'''
