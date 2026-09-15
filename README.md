Restaurant Bill Generator

A simple terminal-based Restaurant Bill Generator built with Python. The program displays a restaurant menu, allows users to select food items and quantities, combines repeated items in the order, calculates the total bill, and applies a discount based on the total amount.

This project is designed as a beginner-level Python practice project for learning:

Functions

Lists

Tuples

User input

if, elif, and else

while loops

for loops

String comparison

String methods

Integer conversion

List indexing

List methods such as append()

Basic calculations

Boolean variables

break

continue

return

Basic program flow

Features

The current version of the program includes:

Display a restaurant welcome message

Display a food menu

Show item numbers and prices

Allow users to select menu items

Allow users to enter item quantities

Validate menu item choices

Validate that quantity is greater than zero

Add selected items to an order

Combine quantities when the same item is selected again

Calculate the total bill

Apply a discount based on the total amount

Support a 5% discount for bills over Rs. 1000

Support a 10% discount for bills over Rs. 2000

Finish the order by entering 0

Menu

When the program starts, it displays the restaurant menu:

--- Welcome to the Restaurant ---
Menu:
1. Burger - Rs. 350
2. Pizza - Rs. 900
3. Pasta - Rs. 650
4. Fries - Rs. 200
5. Cold Drink - Rs. 100
6. Sandwich - Rs. 300
0. Finish Order


The menu is stored in a list:

menu = [
    ("Burger", 350),
    ("Pizza", 900),
    ("Pasta", 650),
    ("Fries", 200),
    ("Cold Drink", 100),
    ("Sandwich", 300),
]


Each menu item is stored as a tuple containing:

Item name

Item price

For example:

("Burger", 350)

Restaurant Bill Generator Function

The main functionality is contained inside the:

def restaurant_bill_generator():


function.

This function controls the restaurant menu, order processing, quantity handling, total calculation, and discount calculation.

Display Menu

The program uses a for loop to display each menu item:

for i in range(len(menu)):
    item, price = menu[i]
    print(f"{i + 1}. {item} - Rs. {price}")


The loop goes through the menu list and displays each item with its number and price.

The program uses:

len(menu)


to determine how many items are in the menu.

It also uses:

i + 1


so that the menu starts from item number 1 instead of 0.

Order Storage

The user's order is stored in a list:

order = []


The total bill is initially set to:

total = 0


When a new item is selected, it is added to the order list.

For example:

order.append([item, qty, price])


An order entry contains:

Item name

Quantity

Price

For example:

["Burger", 2, 350]

Taking User Input

The program repeatedly asks the user to select an item:

choice = input("\nEnter item number to add to order (0 to finish): ")


The user can enter:

1 for Burger

2 for Pizza

3 for Pasta

4 for Fries

5 for Cold Drink

6 for Sandwich

0 to finish the order

While Loop

The order system uses a while True loop:

while True:


This allows the user to continue adding items until they choose:

0


When the user enters 0, the loop stops using:

break


Example:

if choice == '0':
    break

Menu Choice Validation

The program checks whether the selected menu number is valid:

if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
    print("Invalid choice. Please select a valid menu item.")
    continue


The program uses:

choice.isdigit()


to check whether the input contains digits.

It also checks whether the number is within the valid menu range.

For example, if the user enters:

9


the program displays:

Invalid choice. Please select a valid menu item.


The continue statement then returns to the beginning of the while loop.

Selecting a Menu Item

After validating the user's choice, the program converts the input to an integer:

index = int(choice) - 1


The - 1 is used because Python list indexes start from 0.

The selected item is then retrieved:

item, price = menu[index]


For example, if the user enters:

1


the program accesses:

("Burger", 350)

Entering Quantity

After selecting an item, the program asks for the quantity:

qty = int(input(f"Enter quantity for {item}: "))


For example:

Enter quantity for Burger: 2


The program then checks whether the quantity is greater than zero:

if qty <= 0:
    print("Quantity must be greater than 0.")
    continue


If the user enters 0 or a negative number, the program rejects the quantity.

Example:

Enter quantity for Burger: 0
Quantity must be greater than 0.

Checking for Existing Items

The program checks whether the selected item is already present in the order:

found = False

for entry in order:
    if entry[0] == item:
        entry[1] += qty
        found = True
        break


The for loop searches through the existing order.

The program compares:

entry[0] == item


If the item is already in the order, its quantity is increased instead of creating another order entry.

For example, if the user first orders:

2 Burgers


and later orders:

3 Burgers


the order quantity becomes:

5 Burgers

Boolean Variable

The program uses a Boolean variable:

found = False


This variable is used to determine whether the selected item was already found in the order.

When a matching item is found:

found = True


If no matching item is found, the program adds a new item:

if not found:
    order.append([item, qty, price])


This demonstrates the use of:

True

False

if

not

Adding Items to the Order

If an item is not already present, it is added to the order:

order.append([item, qty, price])


The append() method adds a new element to the list.

For example:

order.append(["Pizza", 2, 900])


The order list could then contain:

[
    ["Burger", 2, 350],
    ["Pizza", 2, 900]
]

Total Bill Calculation

The program calculates the cost of each selected item using:

total += qty * price


For example, if the user orders:

2 Burgers


and one Burger costs Rs. 350:

2 × 350 = Rs. 700


The amount is added to the total bill.

Order Confirmation

After adding an item, the program displays:

print(f"Added {qty} x {item} to your order.")


For example:

Added 2 x Burger to your order.

Discount Calculation

After the order is finished, the program calculates a discount based on the total amount.

The initial discount is:

discount_percent = 0


If the total is greater than Rs. 2000:

if total > 2000:
    discount_percent = 10


The customer receives a 10% discount.

If the total is greater than Rs. 1000:

elif total > 1000:
    discount_percent = 5


The customer receives a 5% discount.

If the total is Rs. 1000 or less, no discount is applied.

Discount Rules
Total Bill	Discount
Rs. 0 - Rs. 1000	0%
Above Rs. 1000	5%
Above Rs. 2000	10%

For example, if:

Total = Rs. 1500


the discount is:

5%


If:

Total = Rs. 2500


the discount is:

10%

Discount Amount

The discount amount is calculated using:

discount_amount = (discount_percent / 100) * total


For example, if the total is Rs. 2000 and the discount is 5%:

5 / 100 × 2000 = Rs. 100


The discount amount is Rs. 100.

Subtotal After Discount

The final amount after applying the discount is calculated using:

subtotal_after_discount = total - discount_amount


For example:

Total: Rs. 2000
Discount: Rs. 100
After Discount: Rs. 1900

Program Flow

The current program follows this general flow:

Define the restaurant_bill_generator() function.

Create the restaurant menu.

Display the welcome message.

Display all menu items.

Create an empty order list.

Set the total bill to 0.

Ask the user to select a menu item.

Validate the menu choice.

Ask for the quantity.

Validate the quantity.

Check whether the item already exists in the order.

Add the item or increase its quantity.

Calculate the total.

Continue asking for items.

Stop when the user enters 0.

Calculate the discount.

Calculate the amount after the discount.

Python Concepts Used

This project practices several Python fundamentals:

Functions

Lists

Tuples

for loops

while loops

if statements

elif statements

continue

break

return

User input with input()

Integer conversion with int()

String comparison

String formatting with f-strings

String methods such as isdigit()

List indexing

List slicing/access

len()

range()

append()

Boolean variables

True and False

Arithmetic operators

Basic bill calculations

Important Note About Dictionaries

Although this project is intended to practice basic Python data structures, the current code does not use dictionaries.

The menu uses tuples inside a list:

menu = [
    ("Burger", 350),
    ("Pizza", 900),
]


The order uses lists inside a list:

order.append([item, qty, price])


A future version could use dictionaries to make the order data easier to understand, for example:

{
    "item": "Burger",
    "quantity": 2,
    "price": 350
}

Current Limitations

The current version has some limitations:

The program does not display the final bill yet.

The order details are not printed after the order is finished.

The discount amount is calculated but not displayed.

The final subtotal is calculated but not displayed.

Quantity input can cause a ValueError if the user enters non-numeric text.

The program does not use dictionaries.

The menu is hard-coded inside the function.

There is no file or database storage.

Orders are lost when the program ends.

There is no option to remove an item from the order.

There is no option to change an item's quantity after adding it.

There is no tax calculation.

There is no receipt-generation feature.

The code shown does not include a function call such as restaurant_bill_generator().

Future Improvements

Possible improvements include:

Display the complete final bill.

Display all ordered items and quantities.

Display the original total.

Display the discount percentage.

Display the discount amount.

Display the final amount to pay.

Add try and except for quantity validation.

Prevent invalid numeric input from crashing the program.

Add a function to display the final receipt.

Add a function to remove items.

Add a function to update quantities.

Use dictionaries for order information.

Add tax calculation.

Add payment functionality.

Save receipts to a file.

Add customer information.

Organize the project into multiple functions.

Add unit tests.

Example

A typical ordering process starts like:

--- Welcome to the Restaurant ---
Menu:
1. Burger - Rs. 350
2. Pizza - Rs. 900
3. Pasta - Rs. 650
4. Fries - Rs. 200
5. Cold Drink - Rs. 100
6. Sandwich - Rs. 300
0. Finish Order

Enter item number to add to order (0 to finish): 1
Enter quantity for Burger: 2
Added 2 x Burger to your order.

Enter item number to add to order (0 to finish): 2
Enter quantity for Pizza: 1
Added 1 x Pizza to your order.

Enter item number to add to order (0 to finish): 0


The program then calculates the total and determines whether a discount should be applied.

Project Purpose

This project is primarily intended for Python practice and learning.

It demonstrates how basic Python concepts can be combined to create a simple interactive terminal application.

The project is useful for practicing:

Functions

Lists

Tuples

Loops

Conditional statements

User input

Input validation

Searching through a list

Updating list data

Arithmetic calculations

Basic program structure

Restaurant order processing

License

This project is intended for educational and practice purposes.