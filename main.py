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
        if not order:
            print("\nNo items ordered. Exiting...")
            return
        discount_percent = 0
    if total > 2000:
        discount_percent = 10
    elif total > 1000:
        discount_percent = 5

    discount_amount = (discount_percent / 100) * total

    subtotal_after_discount = total - discount_amount
    tax_percent = 5
    tax_amount = (tax_percent / 100) * subtotal_after_discount

    grand_total = subtotal_after_discount + tax_amount

    print("BILL RECEIPT ")
    print(f"{'Item':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
    print("-" * 40)
    for item, qty, price in order:
        item_total = qty * price
        print(f"{item:<15}{qty:<5}{price:<10}{item_total:<10}")
    print("-" * 40)
    print(f"Subtotal: Rs. {total}")
    print(f"Discount ({discount_percent}%): -Rs. {discount_amount:.2f}")
    print(f"Tax ({tax_percent}%): +Rs. {tax_amount:.2f}")
    print(f"Grand Total: Rs. {grand_total:.2f}")
    print("=================================")
    print("Thank you for dining with us!")