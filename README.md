Restaurant Bill Generator

A simple terminal-based Restaurant Bill Generator built with Python.

The program displays a restaurant menu, allows the user to select food items and quantities, stores the order in a list, combines repeated items, calculates the total bill, applies a discount, calculates 5% tax, and displays a complete final bill receipt.

This project is designed as a beginner-level Python practice project for learning fundamental Python concepts through a practical application.

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

Calculate the original subtotal

Apply a discount based on the total

Calculate the discount amount

Calculate the subtotal after discount

Calculate 5% tax

Calculate the final grand total

Display a complete bill receipt

Display ordered items, quantities, prices, and item totals

Finish the order by entering 0

Display a thank-you message after the bill

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


Here:

"Burger" is the item name.

350 is the item price.

Main Function

The main program is contained inside the following function:

def restaurant_bill_generator():


This function handles:

Menu creation

Menu display

Customer input

Menu choice validation

Quantity validation

Order processing

Repeated item handling

Total calculation

Discount calculation

Tax calculation

Receipt generation

Final grand total

The function is called at the end of the program:

restaurant_bill_generator()


This starts the Restaurant Bill Generator when the Python file is executed.

Displaying the Menu

The program uses a for loop to display all menu items:

for i in range(len(menu)):
    item, price = menu[i]
    print(f"{i + 1}. {item} - Rs. {price}")


The len() function determines the number of items in the menu.

The range() function generates the required indexes.

Python list indexes start at 0, but menu numbers displayed to the customer start at 1.

Therefore, the program uses:

i + 1


For example:

Python Index     Menu Number
0                1
1                2
2                3

Order Storage

The customer's order is stored in an empty list:

order = []


The total bill is initially:

total = 0


Each order entry is stored as a list containing:

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

The program asks the customer to select a menu item:

choice = input("\nEnter item number to add to order (0 to finish): ")


The user can enter:

1 to 6 to select a menu item

0 to finish the order

Example:

Enter item number to add to order (0 to finish): 1

While Loop

The program uses:

while True:


This allows the customer to continue adding items until they choose to finish the order.

When the customer enters 0:

if choice == '0':
    break


The break statement exits the ordering loop.

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


The continue statement skips the current loop iteration and asks the customer for another choice.

Selecting an Item

After validating the menu choice, the program calculates the list index:

index = int(choice) - 1


The selected item is then retrieved:

item, price = menu[index]


For example, if the customer selects:

1


the program retrieves:

("Burger", 350)

Entering Quantity

The program asks the customer for the quantity:

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


For example, if the customer first orders:

2 Burgers


and later orders:

3 Burgers


the order becomes:

5 Burgers


instead of creating two separate Burger entries.

Boolean Variable

The program uses:

found = False


to keep track of whether an item already exists in the order.

When an item is found:

found = True


If the item is not found, a new order entry is added:

if not found:
    order.append([item, qty, price])


This demonstrates the use of:

True

False

not

Boolean variables

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


The amount is added to the original total.

After an item is successfully added, the program displays:

print(f"Added {qty} x {item} to your order.")


Example:

Added 2 x Burger to your order.

Discount Calculation

After the customer finishes the order, the program calculates a discount.

The discount initially starts at:

discount_percent = 0


If the total is greater than Rs. 2000:

if total > 2000:
    discount_percent = 10


The customer receives a 10% discount.

If the total is greater than Rs. 1000:

elif total > 1000:
    discount_percent = 5


The customer receives a 5% discount.

Otherwise, no discount is applied.

Discount Rules
Original Total	Discount
Rs. 1000 or less	0%
Above Rs. 1000	5%
Above Rs. 2000	10%

The conditions use > rather than >=.

Therefore:

Rs. 1000 → 0%

Above Rs. 1000 → 5%

Rs. 2000 → 5%

Above Rs. 2000 → 10%

Discount Amount

The discount amount is calculated using:

discount_amount = (discount_percent / 100) * total


For example, if the original total is Rs. 1500:

Discount = 5%

Discount Amount = (5 / 100) × 1500
                = Rs. 75

Subtotal After Discount

The discount is subtracted from the original total:

subtotal_after_discount = total - discount_amount


For example:

Original Total:          Rs. 1500
Discount:                Rs. 75
Subtotal After Discount: Rs. 1425

Tax Calculation

The program applies a 5% tax after the discount:

tax_percent = 5


The tax amount is calculated using:

tax_amount = (tax_percent / 100) * subtotal_after_discount


For example:

Subtotal After Discount = Rs. 1425
Tax = 5%

Tax Amount = (5 / 100) × 1425
           = Rs. 71.25

Grand Total

The final amount is calculated using:

grand_total = subtotal_after_discount + tax_amount


For example:

Subtotal After Discount: Rs. 1425
Tax:                     Rs. 71.25
Grand Total:             Rs. 1496.25


The grand_total represents the final amount that the customer needs to pay.

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

Final Bill Receipt

The updated version displays a complete receipt.

The receipt displays:

Item

Quantity

Price

Item total

Original subtotal

Discount percentage

Discount amount

Tax percentage

Tax amount

Grand total

The receipt header is formatted using:

print(f"{'Item':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")


The program then loops through the order:

for item, qty, price in order:
    item_total = qty * price
    print(f"{item:<15}{qty:<5}{price:<10}{item_total:<10}")


Each item's total is calculated using:

item_total = qty * price


Example receipt:

BILL RECEIPT
Item           Qty  Price     Total
----------------------------------------
Burger         2    350       700
Pizza          1    900       900
----------------------------------------
Subtotal: Rs. 1600
Discount (5%): -Rs. 80.00
Tax (5%): +Rs. 76.00
Grand Total: Rs. 1596.00
=================================
Thank you for dining with us!

Program Flow

The program follows this general flow:

Define the restaurant_bill_generator() function.

Create the restaurant menu.

Display the welcome message.

Display all menu items.

Create an empty order list.

Set the total bill to 0.

Ask the user to select an item.

Validate the menu choice.

Get the selected item and price.

Ask the user for a quantity.

Validate the quantity.

Search for an existing item in the order.

Update the existing quantity or add a new order entry.

Calculate the item cost.

Add the cost to the total.

Continue accepting items.

Finish the order when the user enters 0.

Calculate the discount.

Calculate the discounted subtotal.

Calculate 5% tax.

Calculate the grand total.

Display the complete bill receipt.

Display a thank-you message.

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

List updating

append()

Boolean variables

True and False

not

Arithmetic operators

Multiplication

Addition

Subtraction

Division

Percentage calculations

f-strings

Formatted output

Basic data processing

Dictionaries

The current version does not use dictionaries.

The menu uses a list containing tuples:

menu = [
    ("Burger", 350),
    ("Pizza", 900),
]


The order uses lists inside a list:

order.append([item, qty, price])


For example:

[
    ["Burger", 2, 350],
    ["Pizza", 1, 900]
]


A future version could use dictionaries to store order information:

{
    "item": "Burger",
    "quantity": 2,
    "price": 350
}

Current Limitations

The current version has some limitations:

Quantity input can cause a ValueError if the user enters non-numeric text.

The menu is hard-coded.

There is no file or database storage.

Orders are lost when the program ends.

There is no option to remove an item.

There is no option to edit an item's quantity.

There is no payment functionality.

There is no receipt-saving functionality.

Tax is fixed at 5%.

Discount rates are hard-coded.

Customer information is not collected.

The program is mainly contained inside one function.

There are no automated unit tests.

The program does not use dictionaries.

Future Improvements

Possible improvements include:

Add try and except for quantity validation.

Prevent invalid quantity input from crashing the program.

Add an option to remove items.

Add an option to update item quantities.

Use dictionaries for storing order information.

Add customer name and contact information.

Add payment functionality.

Support different payment methods.

Save receipts to a text file.

Add customizable tax rates.

Add customizable discount rules.

Add more menu items.

Allow customers to view their current order before checkout.

Organize the project into multiple functions.

Add unit tests.

Add receipt numbering.

Add date and time to receipts.

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


The program then generates a receipt similar to:

BILL RECEIPT
Item           Qty  Price     Total
----------------------------------------
Burger         2    350       700
Pizza          1    900       900
----------------------------------------
Subtotal: Rs. 1600
Discount (5%): -Rs. 80.00
Tax (5%): +Rs. 76.00
Grand Total: Rs. 1596.00
=================================
Thank you for dining with us!

Complete Bill Calculation Example

Suppose the customer orders:

2 Burgers
1 Pizza


The calculation is:

Burger:
2 × Rs. 350 = Rs. 700

Pizza:
1 × Rs. 900 = Rs. 900

Original Total:
Rs. 700 + Rs. 900 = Rs. 1600


Since the total is above Rs. 1000, the customer receives a 5% discount:

Discount:
5% of Rs. 1600 = Rs. 80

Subtotal After Discount:
Rs. 1600 - Rs. 80 = Rs. 1520


Tax is then calculated:

Tax:
5% of Rs. 1520 = Rs. 76


Finally:

Grand Total:
Rs. 1520 + Rs. 76 = Rs. 1596

How to Run

Make sure Python is installed on your computer.

Save the program as:

restaurant_bill_generator.py


Then run it from the terminal:

python restaurant_bill_generator.py


The program will display the restaurant menu and ask you to enter your order.

Enter 0 when you are finished ordering.

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

Boolean variables

String methods

f-strings

Formatted output

Basic program structure

Restaurant order processing

Receipt generation

License

This project is intended for educational and practice purposes.