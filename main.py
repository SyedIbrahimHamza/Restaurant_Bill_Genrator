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