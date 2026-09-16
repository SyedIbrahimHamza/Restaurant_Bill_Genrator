Restaurant Bill Generator

A simple terminal-based Restaurant Bill Generator built with Python.

This program allows users to select food items, enter quantities, combine repeated items, calculate the bill, apply discounts and tax, and print a final receipt.

Features

Display restaurant menu

Select food items

Enter item quantity

Validate menu choices

Validate quantity

Combine repeated items

Calculate total bill

Apply discount

Calculate 5% tax

Print final bill receipt

Finish order by entering 0

Menu
1. Burger - Rs. 350
2. Pizza - Rs. 900
3. Pasta - Rs. 650
4. Fries - Rs. 200
5. Cold Drink - Rs. 100
6. Sandwich - Rs. 300
0. Finish Order

Discount Rules
Total Bill	Discount
Rs. 1000 or less	0%
Above Rs. 1000	5%
Above Rs. 2000	10%

A 5% tax is applied after the discount.

Example
Enter item number to add to order (0 to finish): 1
Enter quantity for Burger: 2
Added 2 x Burger to your order.

Enter item number to add to order (0 to finish): 2
Enter quantity for Pizza: 1
Added 1 x Pizza to your order.

Enter item number to add to order (0 to finish): 0

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

Python Concepts Used

This project practices:

Functions

Lists and tuples

if, elif, else

for and while loops

break and continue

User input

Input validation

int(), isdigit(), len() and range()

List indexing

append()

Boolean variables

Arithmetic operations

Percentage calculations

f-strings

How to Run

Save the program as:

restaurant_bill_generator.py


Then run:

python restaurant_bill_generator.py

Purpose

This project is created for Python practice and learning. It helps beginners understand basic Python concepts by building a simple restaurant billing application.

License

This project is intended for educational and practice purposes.