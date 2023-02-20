#******************************************************************************
# Author:           John Boback, Levi Larkin, Jake Prichard
# Lab:              4
# Date:             02/05/2023
# Description:      ATM program with error handling
# Input:            1-4 for choice of ATM options and amounts for deposit/
#                   withdrawal
# Output:      Balance          
#******************************************************************************


#Import the values from the other 2 Py files. valid.py and functions.py 

import valid as v
import functions as f

# The program will quit out and end if the use enter 4 on the first prompt

QUIT = 4

""" 
This first part of the program defines the default values then displays the messages for what the user inputs in the functions part of the program. then it will display the corrisponding message based on their choise. depending on what choise it is the user will have to input a deposit or withdraw amount. if they input options 1 or 4 either their balance will show or it will give a exit message as the program ends. 
"""

def main():
    choice = 0
    balance = 0.0
    # Define values

    print("Welcome to JJL Credit Union")
    #Print welcome message
    f.print_menu()

    while choice != QUIT:
# Start while loop, call the get choice function from the valid module to get the choice from the user.
        choice = v.get_choice()
        if choice == 1:
            f.view_balance(balance)
# Have user view their bank balance. Call the view balance function from the functions module.  
        elif choice == 2:
            print("Please enter a positive deposit amount: ")
            deposit = v.get_deposit_amt()
            balance = balance + deposit
            print(f"Your balance is now ${balance:.2f}")
            f.print_menu()
# Have user deposit their money.  Call the get deposit amount function from the valid module. Reprint the menu.
        elif choice == 3:
            print("Please enter a positive withdrawal amount: ")
            withdraw = v.get_withdraw_amt(balance)
            balance -= withdraw
            print(f"Your balance is now ${balance:.2f}")
            f.print_menu()
# Have user withdraw their money.  Call the get withdraw amount function from the functions module.  reprint menu.

    print("\nThank you for using JJL Credit Union!")



main()
