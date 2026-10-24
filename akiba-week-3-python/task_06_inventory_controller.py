inventory = []        


def find_product(name):
    """Return the product dict with this name, or None."""
    for product in inventory:
        if product["name"] == name:
            return product
    return None


def add_product(name, price, stock):
    if name == "":
        print("Rejected: product name cannot be empty.")
        return
    if find_product(name) is not None:
        print("Rejected: product already exists:", name)
        return
    if price < 0:
        print("Rejected: price cannot be negative.")
        return
    if stock < 0:
        print("Rejected: stock cannot be negative.")
        return

    inventory.append({"name": name, "price": price, "stock": stock})
    print("Added product:", name)


def search_product(name):
    product = find_product(name)
    if product is None:
        print("Not found:", name)
    else:
        print("Found:", product)
    return product


def update_price(name, new_price):
    product = find_product(name)
    if product is None:
        print("Not found:", name)
        return
    if new_price < 0:
        print("Rejected: price cannot be negative.")
        return
    product["price"] = new_price
    print("Updated price of", name, "to", new_price)


def increase_stock(name, amount):
    product = find_product(name)
    if product is None:
        print("Not found:", name)
        return
    if amount <= 0:
        print("Rejected: amount must be more than 0.")
        return
    product["stock"] = product["stock"] + amount
    print("Added", amount, "to stock of", name, "New stock:", product["stock"])


def sell_product(name, quantity):
    product = find_product(name)
    if product is None:
        print("Not found:", name)
        return
    if quantity <= 0:
        print("Rejected: quantity must be more than 0.")
        return
    if quantity > product["stock"]:
        print("Rejected: not enough stock. Available:", product["stock"])
        return
    product["stock"] = product["stock"] - quantity
    total = quantity * product["price"]
    print("Sold", quantity, "of", name, "for", total, "New stock:", product["stock"])


def total_inventory_value():
    total = 0
    for product in inventory:
        total = total + product["price"] * product["stock"]
    print("Total inventory value:", total)
    return total


def low_stock_report(threshold=5):
    """Challenge: threshold is configurable (defaults to 5)."""
    print("Low-stock report (fewer than", threshold, "units):")
    found = False
    for product in inventory:
        if product["stock"] < threshold:
            print("  -", product["name"], "stock:", product["stock"])
            found = True
    if not found:
        print("  (no low-stock products)")


add_product("Apple", 1.5, 10)
add_product("Banana", 0.5, 3)
add_product("Cherry", 5.0, 2)
add_product("Apple", 2.0, 5)        
add_product("", 1.0, 5)           
add_product("Date", -1, 5)          
add_product("Fig", 2.0, -3)        

print("")
search_product("Banana")
search_product("Mango")             

print("")
update_price("Banana", 0.75)
update_price("Mango", 1.0)         

print("")
increase_stock("Apple", 5)
sell_product("Apple", 3)
sell_product("Cherry", 10)          
sell_product("Mango", 1)            

print("")
total_inventory_value()
print("")
low_stock_report()                  
print("")
low_stock_report(10)                