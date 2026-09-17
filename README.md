# Restaurant Bill Generator

A simple terminal-based Restaurant Bill Generator built with Python.

This program allows users to view a restaurant menu, select food items, enter quantities, combine repeated items, calculate the subtotal, apply discounts, calculate 5% tax, and print a final bill receipt.

## Features

* Display restaurant menu
* Select food items
* Enter item quantity
* Validate menu choices
* Validate quantity input
* Prevent invalid or zero quantities
* Combine repeated items
* Calculate subtotal
* Apply automatic discount
* Calculate 5% tax after discount
* Print formatted bill receipt
* Finish order by entering `0`
* Handle empty orders

## Menu

| No. | Item         |   Price |
| --- | ------------ | ------: |
| 1   | Burger       | Rs. 350 |
| 2   | Pizza        | Rs. 900 |
| 3   | Pasta        | Rs. 650 |
| 4   | Fries        | Rs. 200 |
| 5   | Cold Drink   | Rs. 100 |
| 6   | Sandwich     | Rs. 300 |
| 0   | Finish Order |       - |

## Discount Rules

Discount is calculated according to the total bill before tax.

| Total Bill       | Discount |
| ---------------- | -------: |
| Rs. 1000 or less |       0% |
| Above Rs. 1000   |       5% |
| Above Rs. 2000   |      10% |

A 5% tax is applied after the discount.

### Bill Calculation

```text
Discount Amount = Total × Discount Percentage / 100

Amount After Discount = Total - Discount Amount

Tax Amount = Amount After Discount × 5 / 100

Grand Total = Amount After Discount + Tax Amount
```

## Example

```text
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

========= BILL RECEIPT =========
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
```

## Repeated Items

If the same item is selected multiple times, the program combines its quantity.

For example:

```text
Burger × 2
Burger × 3
```

will be displayed as:

```text
Burger × 5
```

The item is shown only once on the final receipt.

## Input Validation

The program validates the menu selection before processing the order.

Example:

```text
Enter item number to add to order (0 to finish): 9

Invalid choice. Please select a valid menu item.
```

The program also validates quantity input.

If the user enters a non-numeric value:

```text
Enter quantity for Burger: abc

Invalid quantity. Please enter a number.
```

If the user enters zero or a negative quantity:

```text
Enter quantity for Burger: 0

Quantity must be greater than 0.
```

## Empty Order

If the user finishes the order without selecting any items, the program displays:

```text
No items ordered. Exiting...
```

The program then exits without generating a bill.

## Python Concepts Used

This project practices the following Python concepts:

* Functions
* Lists
* Tuples
* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* `break`
* `continue`
* User input with `input()`
* Input validation
* `int()`
* `isdigit()`
* `len()`
* `range()`
* List indexing
* `append()`
* Boolean variables
* Arithmetic operations
* Percentage calculations
* f-strings

## How the Program Works

1. The program displays the restaurant menu.
2. The user selects a menu item.
3. The program validates the selected item number.
4. The user enters the quantity.
5. The program validates the quantity.
6. The selected item is added to the order.
7. If the item already exists, its quantity is increased.
8. The user can continue adding items.
9. Entering `0` finishes the order.
10. The program checks whether any items were ordered.
11. The subtotal is calculated.
12. The appropriate discount is applied.
13. A 5% tax is calculated after the discount.
14. The final bill is displayed.

## Project Structure

```text
restaurant-bill-generator/
│
├── restaurant_bill_generator.py
└── README.md
```

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Save the Program

Save the Python file as:

```text
restaurant_bill_generator.py
```

### 3. Run the Program

Open a terminal in the project directory and run:

```bash
python restaurant_bill_generator.py
```

## Possible Improvements

Future versions could include:

* Remove items from the order
* Update item quantities
* Customer name
* Table number
* Order number
* Date and time
* Payment method
* Save receipt to a file
* More menu categories
* Different tax rates
* Database integration
* Graphical user interface
* Unit testing

## Purpose

This project is created for Python practice and learning.

It helps beginners understand how basic Python concepts can be combined to build a practical terminal-based restaurant billing application.

## License

This project is intended for educational and practice purposes.
