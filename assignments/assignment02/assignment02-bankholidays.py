# write a program that prints out the dates of all the bank holidays in Northern Ireland
# Author : Dave Byrne :)
# References:
# https://www.w3schools.com/python/python_json.asp
# https://www.digitalocean.com/community/tutorials/python-pretty-print-json



import json

# load the JSON data from the file
with open('assignments/assignment02/bank_holidays.json') as f:
    data = json.load(f)

# finding the bank holidays for just Northern Ireland
ni_holidays = data['northern-ireland']['events']

# first instruction
'''
# print out dates of bank holidays in Northern Ireland
for event in ni_holidays:
    print(event["title"], "-", event["date"])'''

# second instruction
# modify program to print bank holidays unique to Northern Ireland that does not
# occur in the rest of the UK

# define bank holidays for UK
uk_holidays = data['england-and-wales']['events'] + data['scotland']['events']

# compare by name
uk_holidays = {event['title'] for event in uk_holidays}

for event in ni_holidays:
    if event['title'] not in uk_holidays:
        print(event["title"], "-", event["date"])

