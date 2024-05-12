def calculate_shipping_charge(num_items):
    if num_items <= 0:
        return "Invalid number of items. Please enter a positive integer."
    elif num_items == 1:
        return 750.00
    else:
        return 750.00 + (num_items - 1) * 200.00
num_items = int(input("Enter the number of items purchased: "))
shipping_charge = calculate_shipping_charge(num_items)
print(f"Shipping charge: {shipping_charge:.2f}")
