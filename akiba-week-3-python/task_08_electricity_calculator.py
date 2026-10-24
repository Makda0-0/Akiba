def calculate_bill(units, service_fee=0):
    if units < 0:
        print("Invalid: units cannot be negative.")
        return

    t1 = min(units, 50) * 0.50

    t2 = max(0, min(units, 150) - 50) * 0.75

    t3 = max(0, units - 150) * 1.20

    total = t1 + t2 + t3 + service_fee

    print("Units:", units)
    print("Tier 1:", t1)
    print("Tier 2:", t2)
    print("Tier 3:", t3)
    print("Service fee:", service_fee)
    print("Total bill:", total)


units = float(input("Enter units consumed: "))
fee = input("Enter service fee (Enter for 0): ")
fee = float(fee) if fee != "" else 0

calculate_bill(units, fee)