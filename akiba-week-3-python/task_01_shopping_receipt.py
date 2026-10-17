items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

def calculate_subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

def calculate_discount(subtotal):
    if subtotal < 0:
        return "needs to be a positive number"
    elif subtotal < 1000:
        return 0
    elif subtotal >= 1000 and subtotal <= 2999:
        return subtotal * 0.05
    elif subtotal >= 3000:
        return subtotal * 0.10

def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate
    return tax

def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    amount = subtotal - discount
    tax = calculate_tax(amount, tax_rate)
    final = amount + tax
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final amount:", final)

generate_receipt(items, 0.15)