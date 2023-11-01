my_dict = {}
lines = input()

while lines != "statistics":
    product, quantity = lines.split(": ")
    quantity = int(quantity)
    if product not in my_dict:
        my_dict[product] = quantity
    else:
        my_dict[product] += quantity

    lines = input()

total_products = len(my_dict)
total_quantity = sum(my_dict.values())

print("Products in stock:")
for keys,values in my_dict.items():
    print(f"- {keys}: {values}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
