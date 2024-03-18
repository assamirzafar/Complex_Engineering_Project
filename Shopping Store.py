from _datetime import datetime

# This is the function for Main screen
def main():
    print()
    print("Note : Do not Press unecessary spacebar and other keys PROGRAM MAY CRASH ! due to int input at some necessary places")
    print()
    print()
    print('                                   PRESS 1 FOR LOGIN                           PRESS 2 TO CREATE ACCOUNT')
    print()

    # Prompting user for choice

    choice = input('Proceed to ==> ')
    if choice == '2':
        # It will call create account function
        create_account()

    elif choice == '1':
        # It will call Login Account function
        login()

    else:
        print()
        print('Invalid Input. Please enter 1 or 2 according to the given choices.')
        main()


# This Function Creates account for new costumers
def create_account():
    print()
    print('Create account')
    print()

    # These are the Input variables for Prompting users for there Credentials

    first_name = input('Enter your first name:        ')
    print()
    last_name = input('Enter your last name:         ')
    print()
    address = input('Enter your address:           ')
    print()
    username = input('Enter username:               ')
    while True:

        # Checking that whether Username exists in data.txt or not

        # Username must be unique so it should not be in data.txt

        if username_exists(username):
            print()
            print('Username already exists. Please choose a different one.')
            print("***************************************************")

            # Prompting user for choice what wants now

            print("Enter a unique username or press 1 to login")
            print()
            print(" Press \'U\' to enter new Username")
            print()
            print("Press 'Enter key' key to create a new account")
            print("***************************************************")

            choice = input('Enter your choice: ')

            print()
            if choice == '1':

                # It will call login function

                login()

            elif choice.upper() == 'U':
                print()

                # Take username again on User's Request

                username = input('Enter your username: ')

            else:

                # Creates New User Account

                create_account()
                break

        else:

            # If username is unique It will Prompt user for Unique Email address

            print()
            email = input('Enter email:                  ')
            while True:

                # Check Whether Email address is unique or not

                if email_exists(email):

                    # Prompting user what he wants now
                    print("*********************************************************")
                    print('Email already exists. Please choose a different one.')
                    print()
                    print('Enter a new email address by pressing \"k\"')
                    print()
                    print('press "1" to login')
                    print()
                    print('press "Enter keys" keys to quit to main screen')
                    print("*********************************************************")

                    choice = input("Enter your Choice: ")

                    print()
                    if choice == '1':

                        # It will Call Login function

                        login()

                    elif choice.lower() == 'k':
                        print()
                        # Prompts User for unique Email

                        email = input('Enter your new email: ')
                    else:

                        # Redirects User to Main Screen

                        main()
                else:

                    # Opens Main data file

                    with open('data.txt', 'a+') as main_data_file:
                        main_data_file.seek(0)
                        file_content = main_data_file.read()

                        # Attempts to load user data from 'data.txt', checks if the loaded data is a dictionary.

                        # And raises an error if it's not.

                        try:
                            users_data_dict = eval(file_content) if file_content else {}
                            if not isinstance(users_data_dict, dict):
                                raise ValueError("Invalid dictionary format in 'data.txt'")
                        except (SyntaxError, ValueError) as e:
                            print(f"Error loading data from 'data.txt': {e}")
                            return

                    # Generates Password for the User

                    password = generate_password(first_name, last_name, username, email)
                    print()
                    print(f'Your Autogenerated password is {password}')

                    # Creates Dictionary of the user Credentials

                    user_dict = {
                        'Email': email,
                        'Password': password,
                        'Username': username,
                        'Address': address,
                        'FirstName': first_name,
                        'LastName': last_name
                    }

                    # Save it as an inner dictionary in Dictionary named as users_data

                    users_data_dict[username] = user_dict

                    # This function will save That dictionary to main file (data.txt)

                    save_main_txt(users_data_dict)
                    print()
                    print('Account created successfully!')
                    login()
                    return



# Function for Checking username whether or not username exist
def username_exists(username):
    with open('data.txt', 'a+') as file:
        file.seek(0)
        file_contents = file.read()
        users_data_dict = eval(file_contents) if file_contents else {}

        if username in users_data_dict:

            return True

    return False

# Function for Checking Email whether or not Email exist
def email_exists(email):
    with open('data.txt', 'a+') as file:
        file.seek(0)
        file_contents = file.read()
        users_data_dict = eval(file_contents) if file_contents else {}

        Emails = list(users_data_dict.keys())

        for i in Emails:
            outer_var = str(users_data_dict.get(i))
            inn_dict = eval(outer_var, {}) if outer_var else {}
            saved_email = inn_dict.get('Email')

            if saved_email == email:

                return True

    return False


# This Function generates Passwords for user
def generate_password(first_name, last_name, username, email):

    return 'cepps' + first_name[1] + last_name[:3] + username[:2] + email[:3]


# This function is for saving the user dictionary named user_data to data.txt
def save_main_txt(users_data_dict):

    with open('data.txt', 'w') as main_data_file:
        main_data_file.write(str(users_data_dict))


# It is the login function
def login():
    print()
    print('Login')
    print()
    while True:
        # Checks username
        if chck_username():
            break



# This Function is to check vaidity of username
def chck_username():

    # Taking Username as Input From User

    username = input("Enter your username: ")

    # Checking That whether Username exist in Program's User records or not

    with open('data.txt', 'a+') as file:
        file.seek(0)
        file_contents = file.read()
        username_dict = eval(file_contents) if file_contents else {}
        username_keys = list(username_dict.keys())


        if username in username_keys:
            # If Username exists it will Prompt user to enter the email associated with that particular email address
            chck_email(username)
            return True

        else:
            print()
            print('Either your Account Doesn\'t exists')

            # Instructions for user
            print("*********************************************************")
            print('Enter a Valid username again by Pressing \"U\"')
            print()
            print('press \"1\" to login')
            print()
            print(' Press \"2\" to Create a New Account')
            print()
            print('Press "Enter Key" to quit to to Main Screen')
            print("*********************************************************")
            print()
            choice = input('Enter'      )

            if choice.upper() == "1":
                login()

            elif choice.upper() == "2":
                create_account()

            elif choice.upper() == "U":
                 chck_username()

            else:
                main()

# This function will Check the validity of Email Address
def chck_email(username):
    print()
    email = input("Enter your email address: ")

    # Checking Email

    with open('data.txt', 'a+') as file:
        file.seek(0)
        file_contents = file.readline()
        data_dict = eval(file_contents) if file_contents else {}
        val = str(data_dict[username].get('Email'))

        if email == val:

            # Now it will Prompt user to enter the Valid Password

            chck_password(username)
            return True

        else:
            print()
            print('Username and Email are not matched !')
            print("*********************************************************")

            # Instructions for user
            print("Enter a Valid Email Address again by Pressing \"U\"")
            print()
            print("press \"1\" to retreat back to login")
            print()
            print('Press "Enter Key" to quit to to Main Screen')
            print("*********************************************************")
            print()
            choice = input("Enter Choice     ")

            if choice.upper() == "1":

                login()

            elif choice.upper() == "U":

                chck_email(username)

            else:

                main()


def chck_password(username):

    with open('data.txt', 'a+') as file:
        file.seek(0)
        file_contents = file.readline()
        data_dict = eval(file_contents) if file_contents else {}
        val = str(data_dict[username].get('Password'))
        print()
        password_attempt = input('Enter your password: ')


        if password_attempt == val:
            print()
            print('Login Successful!')
            print()
            print('Welcome to Our Store')
            print("*********************************************************************")
            print()
            print("To view your shopping history Press 'H'")
            print()
            print("To start shopping Press 'Enter key'")
            print()
            print("*********************************************************************")
            choice = input("Enter your choice ")

            if choice.upper() == "H":
                with (open(f'{username}.txt', 'a+')) as f:
                    f.seek(0)
                    file_contents = f.read()

                    # Check whether history is available or not

                    if len(file_contents) != 0:
                        view_history(username)


                    else:
                        print("*********************************************************")
                        print('No history Available')
                        print()
                        print("Press '1' to LOGOUT'")
                        print()
                        print('Press "Enter key" to do SHOPPING')
                        print("*********************************************************")
                        print()
                        choice = input("Enter your choice ")

                        if choice.upper() == "1":
                            main()

                        else:
                            print('Select the products you want to purchase')
                            print()

                            # Printing Product list

                            print("-------------------------------------------------------------------------------------------")
                            print('|  1) Ketchup Rs 350/-    |     2) Tooth Paste Rs 120/-    |    3) Book Rs 450/-          |')
                            print("-------------------------------------------------------------------------------------------")
                            print('|  4) Brush Rs 50/-       |     5) pencil Rs 10/-          |    6) Pen Rs 20/-            |')
                            print("------------------------------------------------------------------------------------------")
                            print('|  7) Eraser Rs 15/-      |     8) EarPods Rs 1500/-       |    9) Rubik\'s Cube Rs 750/-  |')
                            print("-------------------------------------------------------------------------------------------")
                            print('| 10)Teddy Bear Rs 600/-  |    11) Juice RS 45/-           |   12) Soap Rs 85/-           |')
                            print("------------------------------------------------------------------------------------------")
                            print()


                            # Initializing user_prod_list & user_Product_Dict for future uses in Product Function

                            user_prod_list = []
                            user_Product_Dict = {}

                            Add_to_cart(username, user_prod_list, user_Product_Dict)



            else:
                print('Select the products you want to purchase')
                print()

                # Printing Product list

                print("-------------------------------------------------------------------------------------------")
                print('|  1) Ketchup Rs 350/-    |     2) Tooth Paste Rs 120/-    |    3) Book Rs 450/-          |')
                print("-------------------------------------------------------------------------------------------")
                print('|  4) Brush Rs 50/-       |     5) pencil Rs 10/-          |    6) Pen Rs 20/-            |')
                print("-------------------------------------------------------------------------------------------")
                print('|  7) Eraser Rs 15/-      |     8) EarPods Rs 1500/-       |    9) Rubik\'s Cube Rs 750/-  |')
                print("-------------------------------------------------------------------------------------------")
                print('| 10)Teddy Bear Rs 600/-  |    11) Juice RS 45/-           |   12) Soap Rs 85/-           |')
                print("-------------------------------------------------------------------------------------------")
                print()

                # Initializing user_prod_list & user_Product_Dict for future uses in Product Function

                user_prod_list = []
                user_Product_Dict = {}

                # Product Function is called

                Add_to_cart(username, user_prod_list,  user_Product_Dict)

        else:
            choice = input('\nIncorrect password! Do you want to continue? [Y/N] or press "C" to create a new account: ')

            if choice.upper() == "N":
                login()
            elif choice.upper() == "Y":
                chck_password(username)
            elif choice.upper() == 'C':
                create_account()



# View history function for user to enable him to see past checkouts
def view_history(username):
    print()
    print(f'Checkout history of {username}\n')
    with(open(f'{username}.txt', 'r')) as history:
        items = history.read()
        print(items)
    choice = input('\nTo do More Shopping Press "1"\n\n to log out press "Enter Key"')

    if choice == "1":
        print()
        print('Select the products you want to purchase')
        print()

        # Printing Product list

        print("-------------------------------------------------------------------------------------------")
        print('|  1) Ketchup Rs 350/-    |     2) Tooth Paste Rs 120/-    |    3) Book Rs 450/-          |')
        print("-------------------------------------------------------------------------------------------")
        print('|  4) Brush Rs 50/-       |     5) pencil Rs 10/-          |    6) Pen Rs 20/-            |')
        print("------------------------------------------------------------------------------------------")
        print('|  7) Eraser Rs 15/-      |     8) EarPods Rs 1500/-       |    9) Rubik\'s Cube Rs 750/-  |')
        print("-------------------------------------------------------------------------------------------")
        print('| 10)Teddy Bear Rs 600/-  |    11) Juice RS 45/-           |   12) Soap Rs 85/-           |')
        print("------------------------------------------------------------------------------------------")
        print()

        # Initializing user_prod_list & user_Product_Dict for future uses in Product Function

        user_prod_list = []
        user_Product_Dict = {}

        Add_to_cart(username, user_prod_list, user_Product_Dict)

    else:
        main()



# It is the add to cart function Which will make user enable to add products in Cart
def Add_to_cart(username,user_prod_list, user_Product_Dict):

    # Two dictionaries as value in one dictionary is key in another

    prod_dict = {1: 'Ketchup', 2: 'Tooth Paste', 3: 'Book', 4: 'Brush', 5: 'Pencil', 6: 'Pen', 7: 'Eraser', 8: 'EarPods', 9: "Rubik's Cube", 10: 'Teddy Bear', 11: 'Juice', 12: 'Soap'}

    pric_dict = {'Ketchup': 350, 'Tooth Paste': 120, 'Book': 450, 'Brush': 50, 'Pencil': 10, 'Pen': 20, 'Eraser': 15, 'EarPods': 1500, "Rubik's Cube": 750, 'Teddy Bear': 600, 'Juice': 45, 'Soap': 85}
    print()

    # Taking in string so that program will not get crashed

    choice = input('Enter your choice: ')
    while True:
        # Typecasting it in Integer
        try :
            choice = int(choice)
        except TypeError:
            print('Invalid choice')
            break

        while choice in prod_dict:
            # Taking in string so that program will not get crashed
            quantity = input('Enter quantity: ')
            while True:

                # Checking that quantity must not be less than or equal to zero as it makes no sense

                if quantity <= "0":
                    print("Invalid quantity. Please Enter the greater than zero Value !")
                    break

                else:

                    # Typecasting it in Integer

                    quantity = int(quantity)
                    # Taking value from one dictionary using choice as a key and then its value as akey in second dict price is obtained
                    price = pric_dict[prod_dict[choice]] * quantity

                    print(f' Rs {price}/-')

                    user_Product_Dict[f'Name: {prod_dict[choice]} Rs:{pric_dict[prod_dict[choice]]}/- x Quantity: {quantity} = Rs:{price}/-'] = price

                    user_prod_list.append(f'Name: {prod_dict[choice]} Rs:{pric_dict[prod_dict[choice]]}/- x Quantity: {quantity} = Rs:{price}/-')

                    print("*********************************************************************")

                    option = input('Do you want to Checkout or Continue to add more products?\n\nFor Checkout Press "C"\n\nTo Add more Products to Cart Press " Enter "\n\nTo Remove any Product Press "R"\n\nTo View Cart Press "V":      ')
                    print("*********************************************************************")
                    if option.upper() == 'C':
                        checkout(username, user_prod_list, user_Product_Dict)
                        break

                    elif option.upper() == "V":
                        view_Cart(user_prod_list, user_Product_Dict, username)
                        break

                    elif option.upper() == 'R':
                        remove_cart(username, user_prod_list, user_Product_Dict)

                    else:
                        print()
                        print("------------------------------------------------------------------------------------------")
                        print('|  1) Ketchup Rs 350/-    |     2) Tooth Paste Rs 120/-    |    3) Book Rs 450/-          |')
                        print("-------------------------------------------------------------------------------------------")
                        print('|  4) Brush Rs 50/-       |     5) pencil Rs 10/-          |    6) Pen Rs 20/-            |')
                        print("------------------------------------------------------------------------------------------")
                        print('|  7) Eraser Rs 15/-      |     8) EarPods Rs 1500/-       |    9) Rubik\'s Cube Rs 750/-  |')
                        print("-------------------------------------------------------------------------------------------")
                        print('| 10)Teddy Bear Rs 600/-  |    11) Juice RS 45/-           |   12) Soap Rs 85/-           |')
                        print("------------------------------------------------------------------------------------------")
                        print()
                        Add_to_cart(username, user_prod_list, user_Product_Dict)
                break


        else:
            print('Please enter Valid Choice !')
            Add_to_cart(username, user_prod_list, user_Product_Dict)
        break

# This function is to enable user to view his cart
def view_Cart(user_prod_list, user_Product_Dict, username):
    print()
    print("Your Cart")

    # Following loop will print all the products in cart in serial numbers

    for i, item in enumerate(user_prod_list, start=1):
        print(f'{i}) {item}')
    print()

    listed = list(user_Product_Dict.values())
    Total_Price = sum(listed)
    print("****************************************")
    print(f'Your Total Price is Rs {Total_Price}/-')
    print()
    print("Press 'Enter' to do do more shopping ")
    print()
    print("Press 'R' to remove more products '")
    print()
    print('Press "C" to do CHECKOUT')
    print("****************************************")
    print()

    choice = input("Enter  ")

    if choice.upper() == 'R':
        remove_cart(username, user_prod_list, user_Product_Dict)
        return
    elif choice.upper() == 'C':
        checkout(username, user_prod_list, user_Product_Dict)
    else:
        print()
        print("------------------------------------------------------------------------------------------")
        print('|  1) Ketchup Rs 350/-    |     2) Tooth Paste Rs 120/-    |    3) Book Rs 450/-          |')
        print("-------------------------------------------------------------------------------------------")
        print('|  4) Brush Rs 50/-       |     5) pencil Rs 10/-          |    6) Pen Rs 20/-            |')
        print("------------------------------------------------------------------------------------------")
        print('|  7) Eraser Rs 15/-      |     8) EarPods Rs 1500/-       |    9) Rubik\'s Cube Rs 750/-  |')
        print("-------------------------------------------------------------------------------------------")
        print('| 10)Teddy Bear Rs 600/-  |    11) Juice RS 45/-           |   12) Soap Rs 85/-           |')
        print("------------------------------------------------------------------------------------------")
        print()
        Add_to_cart(username, user_prod_list, user_Product_Dict)
        return


# This function will enable the user to remove any product from cart
def remove_cart(username, user_prod_list,user_Product_Dict):
    print()

    # Following loop will print all the products in cart in serial numbers

    for i, item in enumerate(user_prod_list, start = 1):
        print(f'{i}) {item}')
        print()
    listed = list(user_Product_Dict.values())
    Total_Price = sum(listed)
    print("*********************************************************************")
    print(f'Your Total Price is Rs {Total_Price}/-')


    chs = input('Remove which product from your current cart? Enter only serial numbers! ')

    while True:
            chs = int(chs)
            if chs in range(1, len(user_prod_list) + 1):

                # Deleting removed product from list as well as dictionary

                p = user_prod_list.pop(chs - 1)

                user_Product_Dict.pop(p)

                print(f'" {p} " removed')
                listed = list(user_Product_Dict.values())
                Total_Price = sum(listed)
                print("*********************************************************************")
                print(f'Your Total Price is  Now Rs {Total_Price}/-')
                print("*********************************************************************")
                g = input('Press " R " to remove More products\n\nPress " Enter " to add more products\n\nPress " C " to checkout ')
                print("*********************************************************************")
                print()
                if g.upper() == 'R':
                    remove_cart(username, user_prod_list, user_Product_Dict)
                    break
                elif g.upper() == 'C':
                    if sum(listed) == 0:
                        print('No Products In Cart')
                        print()
                        print("------------------------------------------------------------------------------------------")
                        print('|  1) Ketchup Rs 350/-    |     2) Tooth Paste Rs 120/-    |    3) Book Rs 450/-          |')
                        print("-------------------------------------------------------------------------------------------")
                        print('|  4) Brush Rs 50/-       |     5) pencil Rs 10/-          |    6) Pen Rs 20/-            |')
                        print("------------------------------------------------------------------------------------------")
                        print('|  7) Eraser Rs 15/-      |     8) EarPods Rs 1500/-       |    9) Rubik\'s Cube Rs 750/-  |')
                        print("-------------------------------------------------------------------------------------------")
                        print('| 10)Teddy Bear Rs 600/-  |    11) Juice RS 45/-           |   12) Soap Rs 85/-           |')
                        print("------------------------------------------------------------------------------------------")
                        print()
                        Add_to_cart(username, user_prod_list, user_Product_Dict)
                    else:
                        checkout(username, user_prod_list, user_Product_Dict)
                        break

                else:
                    print()
                    print("------------------------------------------------------------------------------------------")
                    print('|  1) Ketchup Rs 350/-    |     2) Tooth Paste Rs 120/-    |    3) Book Rs 450/-          |')
                    print("-------------------------------------------------------------------------------------------")
                    print('|  4) Brush Rs 50/-       |     5) pencil Rs 10/-          |    6) Pen Rs 20/-            |')
                    print("------------------------------------------------------------------------------------------")
                    print('|  7) Eraser Rs 15/-      |     8) EarPods Rs 1500/-       |    9) Rubik\'s Cube Rs 750/-  |')
                    print("-------------------------------------------------------------------------------------------")
                    print('| 10)Teddy Bear Rs 600/-  |    11) Juice RS 45/-           |   12) Soap Rs 85/-           |')
                    print("------------------------------------------------------------------------------------------")
                    print()
                    Add_to_cart(username, user_prod_list, user_Product_Dict)
                break

            else:
                chs = input('Invalid entry. Please enter a valid serial number: ')


# Checkout Function
def checkout(username, user_prod_list, user_Product_Dict):
    print('Checking out')
    print()
    print("Following is your Finalized cart")
    print()

    for i, item in enumerate(user_prod_list, start = 1):
        print(f'{i}) {item}')
        print()
    listed = list(user_Product_Dict.values())
    Total_Price = sum(listed)
    print("*********************************************************************")
    print(f'Your Total Price is Rs {Total_Price}/-')
    print("*********************************************************************")

    print("*********************************************************************")

    choice = input('To Place Order Type " OK "\n\nTo Remove Any Product " R "\n\nTo Add a Product press Any Key\n\nEnter:      ')
    print("*********************************************************************")
    print()

    if choice.upper() == 'OK':
        # user_Product_Dict values are the quantity multiplied prices of selected products

        listed = list(user_Product_Dict.values())

        # sum up all the individual prices
        Total_Price = sum(listed)
        print("*********************************************************************")
        print(f'Now Your Total Price is Rs {Total_Price}/-')
        print()
        # Taking Card Info

        while True:
            Card_Number = input('Enter your Card number ')
            if len(Card_Number) > 0 and int(Card_Number) >= 0:
                with (open(f'{username}.txt', 'a+') as file_m):

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    file_m.write("============================================================================================")

                    file_m.write('\n'+str(timestamp))
                    for i in user_prod_list:
                        file_m.write('\n'+str(i))
                    file_m.write('\n---------------------------------\n')
                    file_m.write(f'\nTotal Price: {Total_Price}\n')
                    file_m.write('\n---------------------------------\n')
                    file_m.write('Card Number: ' + Card_Number + '\n\n')

                    file_m.write("============================================================================================")
                Addr = input('Enter your Address ')
                print(f'Your Order has been Placed!\n\nYour Order will be Delivered in just 4 Working Days at your Address {Addr}\n\nPLease Come Again!')
                print()
                print("*********************************************************************")
                break

            else:
                print('Enter Valid Card number')

        print()
        print('Do you want to do more Shopping or LOGOUT?')
        print()
        choice2 = input('Press " 1 " to Shop\n\nPress " Enter " to Logout\n\nPress "H" to view yor shopping history: ')
        if choice2 == '1':
            user_prod_list = []
            user_Product_Dict = {}
            print()
            print("Welcome Back!")
            print("------------------------------------------------------------------------------------------")
            print('|  1) Ketchup Rs 350/-    |     2) Tooth Paste Rs 120/-    |    3) Book Rs 450/-          |')
            print("-------------------------------------------------------------------------------------------")
            print('|  4) Brush Rs 50/-       |     5) pencil Rs 10/-          |    6) Pen Rs 20/-            |')
            print("------------------------------------------------------------------------------------------")
            print('|  7) Eraser Rs 15/-      |     8) EarPods Rs 1500/-       |    9) Rubik\'s Cube Rs 750/-  |')
            print("-------------------------------------------------------------------------------------------")
            print('| 10)Teddy Bear Rs 600/-  |    11) Juice RS 45/-           |   12) Soap Rs 85/-           |')
            print("------------------------------------------------------------------------------------------")
            print()
            Add_to_cart(username, user_prod_list, user_Product_Dict)

        elif choice2.upper() == "H":
            view_history(username)

        else:
            print()
            print("You Were Logged out")
            print()
            main()
    elif choice.upper() == 'R':
        remove_cart(username, user_prod_list, user_Product_Dict)
    else:
        print()
        print("------------------------------------------------------------------------------------------")
        print('|  1) Ketchup Rs 350/-    |     2) Tooth Paste Rs 120/-    |    3) Book Rs 450/-          |')
        print("-------------------------------------------------------------------------------------------")
        print('|  4) Brush Rs 50/-       |     5) pencil Rs 10/-          |    6) Pen Rs 20/-            |')
        print("------------------------------------------------------------------------------------------")
        print('|  7) Eraser Rs 15/-      |     8) EarPods Rs 1500/-       |    9) Rubik\'s Cube Rs 750/-  |')
        print("-------------------------------------------------------------------------------------------")
        print('| 10)Teddy Bear Rs 600/-  |    11) Juice RS 45/-           |   12) Soap Rs 85/-           |')
        print("------------------------------------------------------------------------------------------")
        print()
        Add_to_cart(username, user_prod_list, user_Product_Dict)



#Initializing main function to execute the programme one by one
print()
print()
print("                                        Assamir Zafar CS-23066 ======== Fasih Ahmed Khan CS-23090 ======== Umar Saleem CS-23042")
print("                                               |___________________________________|___________________________________|           ")
print('                                                                           Shopping Store')
print()
main()

