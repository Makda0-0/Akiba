
count = 0

for i in range(3):
    pin = int(input(f"Enter your ATM pin (4 digits): {3 - count} attempts left: "))

    if pin == 1234:
        print("Access granted.")
        print(f"Attempts remaining: {3 - count}")
        break
       
    else:
       count+=1
    if count < 3:
       print("Incorrect pin. Try again.")
       print(f"Attempts remaining: {3 - count}")
    else:
       print("Access denied. You have exceeded the maximum number of attempts.")

    




             
       
        
        