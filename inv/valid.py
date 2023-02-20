"""Functions: getInteger(prompt='>')-Functions in this module pertain to input validation"""

def getInteger(prompt= "> "):
    num = 0
    while True:
        try:
            num = int(input(prompt))
            return num
        except:
            print("Invalid integer. Please try again")
"""getInteger(prompt='>')Takes a user input and validates it as an integer
Param: prompt(optional'>') 
Return: num(integer)"""
  
