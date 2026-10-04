customer_name=input("Enter your name: ")

product_name=input("Enter the First product name: ")
price=float(input("Enter the price of the product: "))
quantity=int(input("Enter the quantity of the product: "))

product_name2=input("Enter the Second product name: ")
price2=float(input("Enter the price of the product: "))
quantity2=int(input("Enter the quantity of the product: "))

total_price1=price*quantity
total_price2=price2*quantity2
total_price=total_price1+total_price2

print("================================")
print("          RECEIPT               ")
print("================================")

print("Customer Name:",customer_name)
print("Product  Price  Qty")
print("----------------------")
print(product_name,"  ",price,"  ",quantity)
print(product_name2,"  ",price2,"  ",quantity2)
print ("Total:",total_price )
print("Thank you for shopping!")
print("================================")