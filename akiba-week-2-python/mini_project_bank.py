balance = 1000
correct_pin = "1234"
transactions = 0


print("===== AKIBA BANK =====")
attempts = 0
pin_ok = False

while attempts < 3:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.")
        pin_ok = True
        break
    else:
        attempts = attempts + 1
        print("Incorrect PIN.")
        print("Attempts remaining:", 3 - attempts)

if pin_ok == False:
    print("Too many incorrect attempts.")
    print("Your account is locked.")
    exit()


running = True

while running:
    print("\n===== AKIBA BANK =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your current balance is:", balance, "Birr")

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid amount. Deposit must be greater than zero.")
        else:
            balance = balance + amount
            transactions = transactions + 1
            print("Deposit successful!")
            print("Your new balance is:", balance, "Birr")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount. Withdrawal must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            transactions = transactions + 1
            print("Withdrawal successful!")
            print("Your new balance is:", balance, "Birr")

    elif choice == "4":
        print("Thank you for using Akiba Bank!")
        print("Goodbye!")
        print("Transactions made:", transactions)
        running = False        # ← stops the loop

    else:
        print("Invalid option.")
        print("Please choose a valid option.")