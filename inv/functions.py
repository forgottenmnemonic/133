import valid as v
"""Functions: Welcome(), printinv(), options(), addItem(), deleteItem()
    -Module contains functions pertaining to the inventory program: A program that tracks inventory items and their 
    quantities"""
inv = {
 "box": 5,
 "big box": 10,
 "massive box": 20
} 

def welcome():
  print("*****Welome to the inventory management system*****")
  print("Would you like to- \n1)start from the existing inventory or \n2)start fresh? ")
  while True:
    new = input("> ")
    if new == "1":
      break
    elif new == "2":
        del inv["box"]
        del inv["big box"]
        del inv["massive box"]
        break
    else:
      print("That is not a proper input- please choose 1 or 2.")
"""welcome(): Void Function
   Param: None
   Return: None"""

def printinv():
  print("Here is your inventory- would you like to make changes?")
  print()
  print("{: <15} {: <15}".format("Item name", "Quantity"))
  print("=====================")
  for x, y in inv.items():
    print("{: <15} {: <15}".format(x, y))
  print("=====================")
  print("{: <15} {: <15}".format("Total Items:", len(inv)))
  print()
"""printinv(): Void Function- Prints the the items of a dictionary, specifically the global dictionary-inv, which 
contains the items and quantity of items already in the inventory.
   Param: None
   Return: None"""
#The printinv() function is called in the options() function.
def options():
  printinv()
  print("Choose 1 to add item")
  print("Choose 2 to delete item")
  print("Choose 3 to quit")
  option = input("> ")
  return option
"""options(): Void function-Prints the inventory list and the options for the user, user input is contained in this function.
Param: None
Return: options(str)"""
def addItem():
  print("Which item would you like to add?")
  x = input("> ")
  print("And the quantity?")
  y = v.getInteger("> ")
  inv[x] = y
"""addItem(): Void Function- Gets an item from the user which is then added to the global dictionary inv.
Param: None
Return: None"""
def deleteItem():
  c=0
  while c==0:
    try:
      print("Which item would you like to delete? Please type the exact name.")
      z = input("> ")
      del inv[z]
    except:
       print("That item does not appear on the list. Remember to type it in exactly as it appears in the list above\n.")
       continue
    c+=1
"""deleteItem(): Voice function-Gets an item that the user would like to delete from the global dictionary-inv.  The user input is then checked against the values in the dictionary, if it is not matched the user is prompted again.
Param:none
Return: none"""  
