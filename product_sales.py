sales = [
    {"region": "North", "product": "Laptop", "amount": 1200},
    {"region": "South", "product": "Laptop", "amount": 900},
    {"region": "North", "product": "Phone", "amount": 800},
    {"region": "North", "product": "Laptop", "amount": 600},
    {"region": "South", "product": "Phone", "amount": None},
    {"region": "East", "product": "Laptop", "amount": 1500},
    {"region": "South", "product": "Laptop", "amount": -200}
]
filtered_sales = []
total_sales = 0
region_totals = {}
products_total = {}
result = {"regions": [], "products":[]}

for every in sales:
    # print(every)
    amount = every["amount"]
    region = every["region"]
    product = every["product"]
    # print(amount)
    if amount is not None and amount > 0 :
        total_sales += amount

        if  region in region_totals:
            region_totals[region] += amount
        else:
            region_totals[region] = amount
    # print(region_totals)

        if product in products_total:
            products_total[product] += amount
            
        else:
            products_total[product] = amount



# region list and prodcut_list
region_list = list(region_totals.items())
product_list = list(products_total.items())
        # print(product_list)
region_list.sort(key=lambda x: x[1], reverse=True)
product_list.sort(key=lambda x: x[1], reverse = True)
        # print(product_list)

result["regions"] = region_list
result["products"] = product_list
result["stats"] = {
            "total_sales":total_sales,
            "top region ": region_list[0][0],
            "top_product": product_list[0][0]
        }

print(result)