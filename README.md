Restaurant Bill Generator

A simple terminal-based Restaurant Bill Generator built with Python. The program displays a restaurant menu, allows the user to select food items and quantities, stores the order in a list, combines repeated items, calculates the total bill, applies a discount, calculates tax, and calculates the final grand total.

This project is designed as a beginner-level Python practice project for learning:

Functions

Lists

Tuples

User input

if, elif, and else

while loops

for loops

Input validation

Integer conversion

String methods

List indexing

List updating

append()

Boolean variables

Arithmetic operations

Percentage calculations

break

continue

return

Basic program flow

Features

The current version of the program includes:

Display a restaurant welcome message

Display the restaurant menu

Display item names and prices

Allow users to select menu items

Allow users to enter quantities

Validate menu item choices

Validate that quantity is greater than zero

Store selected items in an order list

Combine quantities for repeated items

Calculate the total bill

Apply a discount based on the total

Calculate the discounted subtotal

Calculate 5% tax

Calculate the final grand total

Finish the order by entering 0

Menu

When the program starts, it displays the following menu:

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


Each menu item is represented by a tuple containing:

Item name

Item price

For example:

("Burger", 350)

Restaurant Bill Generator

The main program is inside the following function:

def restaurant_bill_generator():


This function handles:

Menu display

Customer input

Order processing

Quantity validation

Order storage

Total calculation

Discount calculation

Tax calculation

Grand total calculation

Displaying the Menu

The program uses a for loop to display all menu items:

for i in range(len(menu)):
    item, price = menu[i]
    print(f"{i + 1}. {item} - Rs. {price}")


The len() function determines the number of items in the menu.

The program uses i + 1 because Python list indexes start at 0, while the menu displayed to the user starts at 1.

Order Storage

The customer's order is stored in an empty list:

order = []


The total bill is initially:

total = 0


Each order is stored as a list containing:

Item name

Quantity

Price

For example:

["Burger", 2, 350]


The order list could contain:

[
    ["Burger", 2, 350],
    ["Pizza", 1, 900]
]

Taking User Input

The program asks the customer to select an item:

choice = input("\nEnter item number to add to order (0 to finish): ")


The user can enter a number from 1 to 6.

The user can enter 0 to finish the order.

Example:

Enter item number to add to order (0 to finish): 1

While Loop

The program uses a while True loop:

while True:


This allows the customer to continue adding items until they choose 0.

When 0 is entered:

if choice == '0':
    break


The break statement stops the loop.

Menu Choice Validation

The program validates the menu choice using:

if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
    print("Invalid choice. Please select a valid menu item.")
    continue


The isdigit() method checks whether the input contains digits.

The program also checks whether the number is within the available menu range.

For example:

Enter item number to add to order (0 to finish): 9
Invalid choice. Please select a valid menu item.


The continue statement skips the current loop iteration and asks for another choice.

Selecting an Item

After validating the menu choice, the program calculates the list index:

index = int(choice) - 1


The selected item is then retrieved:

item, price = menu[index]


For example, if the user selects:

1


the program retrieves:

("Burger", 350)

Entering Quantity

The program asks the user for the quantity:

qty = int(input(f"Enter quantity for {item}: "))


Example:

Enter quantity for Burger: 2


The program then checks whether the quantity is greater than zero:

if qty <= 0:
    print("Quantity must be greater than 0.")
    continue


If the user enters 0 or a negative number, the program rejects the quantity.

Example:

Enter quantity for Burger: 0
Quantity must be greater than 0.

Checking for Repeated Items

The program checks whether the selected item already exists in the order:

found = False

for entry in order:
    if entry[0] == item:
        entry[1] += qty
        found = True
        break


The for loop searches through the existing order.

If the same item is found, its quantity is increased:

entry[1] += qty


For example, if the customer orders:

2 Burgers


and later orders:

3 Burgers


the program combines them into:

5 Burgers


instead of creating two separate Burger entries.

Boolean Variable

The program uses:

found = False


to track whether an item was found in the order.

When an item is found:

found = True


If the item is not found, a new order entry is added:

if not found:
    order.append([item, qty, price])


This demonstrates the use of:

Boolean values

True

False

not

Conditional statements

Adding Items to the Order

The append() method is used to add a new item:

order.append([item, qty, price])


For example:

order.append(["Pizza", 2, 900])


The order list can then contain:

[
    ["Burger", 2, 350],
    ["Pizza", 2, 900]
]

Total Bill Calculation

The cost of each selected item is calculated using:

total += qty * price


For example:

2 Burgers × Rs. 350 = Rs. 700


The amount is added to the total bill.

After adding an item, the program displays:

print(f"Added {qty} x {item} to your order.")


Example:

Added 2 x Burger to your order.

Discount Calculation

After the customer finishes the order, the program calculates a discount.

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
Rs. 1000 or less	0%
Above Rs. 1000	5%
Above Rs. 2000	10%
Discount Amount

The discount amount is calculated using:

discount_amount = (discount_percent / 100) * total


For example, if the total bill is Rs. 1500:

Discount = 5%

Discount Amount = 5 / 100 × 1500
                = Rs. 75

Subtotal After Discount

The program subtracts the discount from the original total:

subtotal_after_discount = total - discount_amount


For example:

Original Total:       Rs. 1500
Discount:             Rs. 75
Subtotal After Discount: Rs. 1425

Tax Calculation

The program applies a 5% tax after the discount:

tax_percent = 5


The tax amount is calculated using:

tax_amount = (tax_percent / 100) * subtotal_after_discount


For example:

Subtotal After Discount = Rs. 1425
Tax = 5%

Tax Amount = Rs. 71.25

Grand Total

The final bill amount is calculated using:

grand_total = subtotal_after_discount + tax_amount


For example:

Subtotal After Discount: Rs. 1425
Tax:                     Rs. 71.25
Grand Total:             Rs. 1496.25


The grand_total represents the final amount after applying the discount and tax.

Bill Calculation Flow

The program calculates the bill in the following order:

Original Total
      ↓
Discount
      ↓
Subtotal After Discount
      ↓
5% Tax
      ↓
Grand Total


The formulas used are:

discount_amount = (discount_percent / 100) * total

subtotal_after_discount = total - discount_amount

tax_amount = (tax_percent / 100) * subtotal_after_discount

grand_total = subtotal_after_discount + tax_amount

Program Flow

The program follows this general flow:

Define the restaurant_bill_generator() function.

Create the restaurant menu.

Display the welcome message.

Display the menu.

Create an empty order list.

Set the total bill to 0.

Ask the user to select an item.

Validate the menu choice.

Get the selected item and price.

Ask the user for quantity.

Validate the quantity.

Search for an existing item.

Update the quantity or add a new item.

Calculate the total.

Continue accepting items.

Finish the order when the user enters 0.

Calculate the discount.

Calculate the discounted subtotal.

Calculate 5% tax.

Calculate the grand total.

Python Concepts Used

This project practices several Python fundamentals:

Functions

Lists

Tuples

for loops

while loops

if statements

elif statements

break

continue

return

User input with input()

Integer conversion with int()

String comparison

isdigit()

len()

range()

List indexing

append()

Boolean variables

True and False

Arithmetic operators

Multiplication

Addition

Subtraction

Division

Percentage calculations

f-strings

Basic data processing

Important Note About Dictionaries

The current version of this project does not use dictionaries.

The menu uses a list containing tuples:

menu = [
    ("Burger", 350),
    ("Pizza", 900),
]


The order uses lists inside a list:

order.append([item, qty, price])


A future version could use dictionaries to store order information.

For example:

{
    "item": "Burger",
    "quantity": 2,
    "price": 350
}

Current Limitations

The current version has some limitations:

The final bill is calculated but not printed.

The order details are not displayed as a final receipt.

The discount amount is calculated but not displayed.

The subtotal after discount is calculated but not displayed.

The tax amount is calculated but not displayed.

The grand total is calculated but not displayed.

Quantity input can cause a ValueError if the user enters non-numeric text.

The program does not use dictionaries.

The menu is hard-coded.

There is no file or database storage.

Orders are lost when the program ends.

There is no option to remove an item.

There is no option to edit an item's quantity.

There is no payment functionality.

There is no receipt-saving functionality.

The code shown does not include a function call such as restaurant_bill_generator().

Future Improvements

Possible improvements include:

Display a complete final receipt.

Display all ordered items.

Display item quantities.

Display item prices.

Display the original total.

Display the discount percentage.

Display the discount amount.

Display the subtotal after discount.

Display the tax percentage.

Display the tax amount.

Display the grand total.

Add try and except for quantity validation.

Prevent invalid quantity input from crashing the program.

Add an option to remove items.

Add an option to update quantities.

Use dictionaries for storing order information.

Add customer information.

Add payment functionality.

Save receipts to a file.

Add tax customization.

Add more menu items.

Organize the project into multiple functions.

Add unit tests.

Example

A typical ordering process looks like:

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


After the order is finished, the program calculates:

Original Total
Discount
Subtotal After Discount
5% Tax
Grand Total

Project Purpose

This project is primarily intended for Python practice and learning.

It demonstrates how basic Python concepts can be combined to create a simple interactive terminal-based restaurant billing application.

The project is useful for practicing:

Functions

Lists

Tuples

Loops

Conditional statements

User input

Input validation

Searching through lists

Updating list data

Arithmetic calculations

Discount calculations

Tax calculations

Basic program structure

Restaurant order processing

License

This project is intended for educational and practice purposes.