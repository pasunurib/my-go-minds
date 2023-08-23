# Initialize lists to store item names and quantities
items = []
quantities = []

# Item prices dictionary
item_prices = {
    "Tea": 10,
    "Coffee": 10,
    "Boost": 15,
    "Lmn.Tea": 15,
    "Milk": 10
}

# Get input from the user
print("-----------TEA-SHOP------------")
print("\t1.Tea (10Rs)")
print("\t2.Coffee (10Rs)")
print("\t3.Boost (15Rs)")
print("\t4.Lmn.Tea (15Rs)")
print("\t5.Milk (10Rs)")
print("---------------------------------------")

while True:
    opt = input("\nPls Enter 'yes' to select an item or type 'bill' to get the bill: ")

    if opt.lower() == "bill":
        break

    if opt.lower() == "yes":
        name = input("Select the item option: ")
        items.append(name)
        qunty = int(input("Enter the quantity: "))
        quantities.append(qunty)

# Print the bill
print("\n\n\t\t\tBILL#00675")
print("-------------------------------------------")
print("ITEM NAME\tWT/QTY\tPRICE\tAMT")
print("-------------------------------------------")

total_amount = 0

for i in range(len(items)):
    item = items[i]
    qty = quantities[i]
    price = item_prices[item]
    amount = price * qty
    total_amount += amount
    print(f"{item}\t\t{qty}\t{price}\t{amount}")

print("-------------------------------------------")
print(f"\t\t\t   Rs   {total_amount}")
print("-------------------------------------------")

# Calculate and print total quantity and number of items
total_quantity = sum(quantities)
num_items = len(items)
print(f"\n  T QTY::  {total_quantity} pcs.")
print(f"  NO OF ITEMS:  {num_items}")

