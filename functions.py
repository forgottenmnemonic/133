
def print_menu():
    """
    Function to print the menu to view balance, make deposit, or withdraw 
    funds
    :return: none
    """
    print("\n1. View balance")
    print("2. Make deposit")
    print("3. Withdraw funds")
    print("4. Quit")
  # Display ATM menu to user

def view_balance(balance):
    """
    Function to print current account balance.
    :param balance: float, current account balance
    :return: none
    """
    print("Account balance: $", format(balance, ".2f"))
    print_menu()
  # Show the account balance of the user
