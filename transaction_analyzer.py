transactions = [
    {"user": "Alice", "amount": 120},
    {"user": "Bob", "amount": -50},
    {"user": "Alice", "amount": 70},
    {"user": "Charlie", "amount": None},
    {"user": "Bob", "amount": 200}
]

filtered_transaction = []
results = {"users":[]}
totals = {}
total_amount = 0
user_list = []

for transaction  in transactions:
    amount = transaction["amount"]
    if amount is not None and amount > 0:
        filtered_transaction.append(transaction)
# print(filtered_transaction)

for transcation in filtered_transaction:
    users_list = []
    user_name = transcation["user"]
    amount = transcation["amount"]
    total_amount += amount


    if user_name in totals:
        totals[user_name] += amount
    else:
        totals[user_name] = amount


for user, amount in totals.items():
#  print(user_list)
  user_list.append((user, amount))
  
user_list.sort(key=lambda x: x[1], reverse=True)


results['users'].append(user_list)

results["stats"] = {
    "total_users" : len(totals),
    "total_amount" : total_amount
}

print(results)