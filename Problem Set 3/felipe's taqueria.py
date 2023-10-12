items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        menu_item = input("Item: ").title().strip()
        if menu_item in items:
            total += items[menu_item]
            print("Total: $", end="")
            print("{:.2f}".format(total))
        else:
            print("Choose from the menu")


    except EOFError:
        print()
        break


