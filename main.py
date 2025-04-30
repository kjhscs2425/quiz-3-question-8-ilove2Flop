import json

# read `expenses.json`
with open('expenses.json', 'r') as file:
    expenses = json.load(file)

# get and print total "price" for all expenses at the "pet store"
total = sum(item['price'] for item in expenses['pet store'])
print(total)

