# Simple Shopping System

## Overview

Welcome to the Simple Shopping System! This basic command-line program, implemented in Python, offers users the ability to create accounts, log in, add products to their cart, and place orders.

## Features
Note : Do not Press unecessary spacebar and other keys PROGRAM MAY CRASH ! due to int input at some necessary places

### Account Management

- New Account Creation:
  Users can create accounts by providing personal details (first name, last name, address, username, and email).
- Password Generation:
  Passwords are automatically generated based on user information.
- Uniqueness Check:
  The system checks for unique usernames and emails to prevent duplicates.

### Login

- User Authentication:
  Users can log in using their username and password.
- Password Validation:
  Passwords are verified during the login process.

### Product Selection

- Dynamic Shopping:
  Users can select products from a predefined list.
- Quantity and Price Calculation:
  The system dynamically calculates quantities and prices based on user selections.

### Shopping Cart

- Cart Management:
  Users can add products to their cart, remove items, and view the current cart.

### Order Placement

- Finalizing Orders:
  Users can complete their shopping, review the total price, and place an order.
- Order Recording:
  Order details, including timestamp, products, total price, and card number, are saved to a user-specific file.

## Usage

1. Run the Program:
   Execute the script in a Python environment.

2. Create Account:
   - Choose option 2 to create a new account.
   - Provide required information and follow the prompts.

3. Login:
   - Choose option 1 to log in.
   - Enter your username and follow the prompts.

4. Product Selection:
   - After logging in, users can select products and add them to the cart.

5. Checkout:
   - Users can finalize the cart, view order details, and place an order.

6. Logout:
   - Choose option Enter to logout.

## Files

- data.txt:
  Stores user data in a dictionary format.

- User-specific Files:
  Each user has a file named `<username>.txt` storing their order history.