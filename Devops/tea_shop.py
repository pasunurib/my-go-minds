
def calculate_bill(tea_price, quantity, tax_rate):
    subtotal = tea_price * quantity
    tax = subtotal * (tax_rate / 100)
    total = subtotal + tax
    return subtotal, tax, total

def print_bill(item_name, quantity, price, subtotal, tax, total):
    print("Tea Shop Bill")
    print("--------------")
    print(f"Item: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Price per unit: ${price:.2f}")
    print("--------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print("--------------")
    print(f"Total: ${total:.2f}")

item_name = "Tea"
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))
tax_rate = float(input("Enter tax rate (%): "))

subtotal, tax, total = calculate_bill(price, quantity, tax_rate)
print_bill(item_name, quantity, price, subtotal, tax, total)
