def restaurant_bill_generator():
    menu = [
        ("Burger", 350),
        ("Pizza", 900),
        ("Pasta", 650),
        ("Fries", 200),
        ("Cold Drink", 100),
        ("Sandwich", 300),
    ]
    print("\n--- Welcome to the Restaurant ---")
    print("Menu:")
    for i in range(len(menu)):
        item, price = menu[i]
        print(f"{i + 1}. {item} - Rs. {price}")
    print("0. Finish Order")

    order = []
    total = 0
    while True:
        choice = input("\nEnter item number to add to order (0 to finish): ")
        if choice == '0':
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
            print("Invalid choice. Please select a valid menu item.")
            continue
        index = int(choice) - 1
        item, price = menu[index]

        qty = int(input(f"Enter quantity for {item}: "))
        if qty <= 0:
            print("Quantity must be greater than 0.")
            continue
        found = False
        for entry in order:
            if entry[0] == item:
                entry[1] += qty
                found = True
                break

        if not found:
            order.append([item, qty, price])

        total += qty * price
        print(f"Added {qty} x {item} to your order.")