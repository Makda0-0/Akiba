
balance = 1000
transactions = []
total_deposited = 0
total_withdrawn = 0
daily_limit = 800
withdrawn_today = 0


def deposit_money(money):
    global balance, total_deposited
    if money <= 0:
        print("Rejected: amount must be more than 0.")
        return
    balance = balance + money
    total_deposited = total_deposited + money
    record_transaction("deposit", money)
    print("Deposited", money, "New balance:", balance)


def withdraw_money(money):
    global balance, total_withdrawn, withdrawn_today
    if money <= 0:
        print("Rejected: amount must be more than 0.")
        return
    if money > balance:
        print("Rejected: not enough money.")
        return
    if money > daily_limit - withdrawn_today:
        print("Rejected: daily limit reached.")
        return
    balance = balance - money
    withdrawn_today = withdrawn_today + money
    total_withdrawn = total_withdrawn + money
    record_transaction("withdrawal", money)
    print("Withdrew", money, "New balance:", balance)


def current_balance():
    print("Current balance:", balance)


def record_transaction(kind, amount):
    transactions.append({
        "type": kind,
        "amount": amount,
        "balance_after": balance
    })


def generate_summary():
    print("")
    print("----- SUMMARY -----")
    print("Total deposited:", total_deposited)
    print("Total withdrawn:", total_withdrawn)
    print("Final balance:", balance)
    print("----- HISTORY -----")
    for t in transactions:
        print(t)
    print("-------------------")


current_balance()
deposit_money(500)
deposit_money(0)
deposit_money(-50)
withdraw_money(300)
withdraw_money(400)
withdraw_money(200)
withdraw_money(5000)
current_balance()
generate_summary()