amount_due = 50

while amount_due > 0:
    print("Amount Due:", "$.",amount_due)
    insert_coin = int(input("Insert coin: "))
    if insert_coin in [25,10,5]:
        amount_due -= insert_coin
    else:
        print("Only 25, 10, or 5, cents")


if amount_due <= 0:
    print("Change owed:", "$.", abs(amount_due))

