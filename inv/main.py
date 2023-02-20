#******************************************************************************
# Author:           John Boback, Levi, Jake Prichard
# Lab:              Lab 05
# Date:             02/12/2023
# Description:      The program asks user to add/remove items to an
#  inventory list.  Users can add items to the list along with the corresponding
# quantity. 
#                   prints a message to the screen.
# Input:            Option (str), Item added (str), item deleted(str).
# Output:           Main menu, updated table of values showing each item/quantity 
# combination in the inventory, Total items in the inventory.
# Sources:          Lab 6 specifications
#                   
#******************************************************************************


import functions as fun

def main():
#Call the welcome function to print welcome message.
  fun.welcome()
  option = 0
#Begin While Loop. 
  while option != "3":
#Call the options function to print the main menu.
    option = fun.options()
#if option 1 is chosen, call the addItem function.
    if option == "1":
      fun.addItem()
#If option 2 is chosen, call the deleteItem function.
    elif option == "2":
      fun.deleteItem()
#If option 3 is chosen, print goodbye message.
    elif option == "3":
      print("Thank you for using our program!")
#If anything else is chosen then print message reminding user of valid inputs.
    else:
      print("Please pick an appropriate number between 1 and 3")

main()
