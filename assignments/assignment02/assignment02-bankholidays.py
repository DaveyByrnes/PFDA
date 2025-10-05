# write a program that prints out the dates of all the bank holidays in Northern Ireland
# Author : Dave Byrne :)
# References:
# https://www.w3schools.com/python/python_json.asp
# https://www.digitalocean.com/community/tutorials/python-pretty-print-json



import json

# load the JSON data from the file
with open('assignments/assignment02/bank_holidays.json') as f:
    data = json.load(f)

print(json.dumps(data, indent=1))