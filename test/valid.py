
"""" The first module for get "get withdraw amount", The user must input a integer that is greater than 0 for the amount to be withdrawn. If the user inputs anything other than a number then the program will kick the user back out and tell them that it is an invalid entry. This is one of the functions that checks for integer input and uses it in the main program. """

def get_withdraw_amt(balance):
  """ 
  Perform error detection for numbers outside of the expected range for the withdrawl.  The function takes one parameter which is used    to determine if the withdraw input is valid (i.e you can't withdrawl more than the balance).
  Parameters: Balance (float)
  Returns: Withdrawl Amount (Integer)
  """
  while True:
    try:
      z = int(input())
      if z <= 0 or z > balance:
        raise ValueError
      print(f"${z} withdrawn")
      break
    except ValueError:
      print("Invalid entry, please try again later with a positive whole number"
      " above your balance")
      z = 0
      break
  return z
  


# Like the previous part 
def get_deposit_amt():
  """
  Performs error detection for numbers outside of the expected range for the deposit. Parameters: None
  Returns: Integer (Deposit Amount)
  """
  while True:
    try:
      y = int(input())
      if y <= 0:
        raise ValueError
      break
    except ValueError:
      print("Invalid entry, please enter a valid positive whole number")
  return y


"""" This part of the program intereacts with that Main python file in providing error checking with the number that the user inputs for the start of the program. the user is give 4 options to choose from. they either have to choose from, view balance, withdraw, deposite or quit. this part ensures that the user can only enter 1-4 as their choise. """

def get_choice():
  """
  Perform error detection for numbers outside of the expected range for selection
      Parameters: None
      Returns: Integer (1-4)
  """
  while True:
    print("What would you like to do?")
    try:
      range_choice = range(1, 5)
      x = int(input())
      if x in range_choice:      
        break
      else:
        print("Invalid entry, please enter a choice from 1-4")
    except:
      print("Invalid entry, please enter a choice from 1-4")
  return x
