# A brief description of the project: This code is for calculating and processes and displays your travel expense(s).
# Also, the words: destination, accommodation, are abbreaviated in those variables to save time and avoid mistakes, also that they wouldn't be too long?!?

# 9/23/2022

# CTI-110 P1HW2 - Travel Expense

# Kelly Bullard

#


# Some info on this program 's code
print('This program calculates and displays travel expences')
print('') # The space in-between the lines

# Inputs for the Travel Expences with output prompts

# User's input for the amount for their budget
print('Enter Budget: ', end='')
amountBudget = int(input())
print('') # The space in-between the lines

# User's input for the travel destination
print('Enter Your travel destination: ', end='') 
travelDestn = input()
print('') # The space in-between the lines

# User's input for the expences' amount of the gas
print('How much do you think you will spend on gas? ', end='')
amountGas = int(input())
print('') # The space in-between the lines

# User's input for the expences' amount for the accomodation
print('Approximately, how much will you need for accomodation/hotel? ', end='')
amountAccomm = int(input())
print('') # The space in-between the lines

# User's input for the expences' amount for food
print('Last, how much do you need for food? ', end='')
amountFood = int(input())
print('') # The space in-between the lines

# Outputs for the Travel Expences

# The outputs and results of the user's inputs
print('------------Travel Expences------------')
print('Location:', travelDestn)
print('Initial Budget:', amountBudget/1.0)
print('') # The space in-between the lines

print('Fuel:', amountGas/1.0)
print('Accomodation:', amountAccomm/1.0)
print('Food:', amountFood/1.0)
print('') # The space in-between the lines

# The calculations of the results of the user's inputs
totalExpences = amountGas + amountAccomm + amountFood
finalBalance = amountBudget - totalExpences
# The over-all expences' amount for the budget for the travel expences
print('Remaining Balance:', finalBalance/1.0)


# Pseudocde for this program's code
# NOTE: For this use the current Python(like Python 3) by using the following inputs and outputs and more for program's code.

# START

# COMMENT: # Some info on this code
# DISPLAY 'This program calculates and displays travel expences'
# DISPLAY '' # COMMENT: # The space in-between the lines

# COMMENT: # Inputs for the Travel Expences with output prompts

# COMMENT: # User's input for the amount for their budget
# DISPLAY 'Enter Budget: ', ADD: end='', to this, so that the user's input is on the same line as the output prompt
# INPUT amountBudget = Integer(input())
# DISPLAY '' # COMMENT: # The space in-between the lines

# COMMENT: # User's input for the travel destination
# DISPLAY 'Enter Your travel destination: ', ADD: end='', to this, so that the user's input is on the same line as the output prompt
# INPUT travelDestn = input()
# DISPLAY '' # COMMENT: # The space in-between the lines

# COMMENT: # User's input for the expences' amount of the gas
# DISPLAY 'How much do you think you will spend on gas? ', ADD: end='', to this, so that the user's input is on the same line as the output prompt
# INPUT amountGas = Integer(input())
# DISPLAY '' # COMMENT: # The space in-between the lines

# COMMENT: # User's input for the expences' amount for the accomodation
# DISPLAY 'Approximately, how much will you need for accomodation/hotel? ', ADD: end='', to this, so that the user's input is on the same line as the output prompt
# INPUT amountAccomm = Integer(input())
# DISPLAY '' # COMMENT: # The space in-between the lines

# COMMENT: # User's input for the expences' amount for food
# DISPLAY 'Last, how much do you need for food? ', ADD: end='', to this, so that the user's input is on the same line as the output prompt
# INPUT amountFood = Integer(input())
# DISPLAY '' # COMMENT: # The space in-between the lines

# COMMENT: # Outputs for the Travel Expences

# COMMENT: # The outputs and results of the user's inputs
# DISPLAY '------------Travel Expences------------'
# DISPLAY 'Location:', travelDestn
# DISPLAY 'Initial Budget:', COMPUTE amountBudget/1.0
# DISPLAY '' # COMMENT: # The space in-between the lines

# DISPLAY 'Fuel:', COMPUTE amountGas/1.0
# DISPLAY 'Accomodation:', COMPUTE amountAccomm/1.0
# DISPLAY 'Food:', COMPUTE amountFood/1.0
# DISPLAY '' # COMMENT: # The space in-between the lines

# COMMENT: # The calculations of the results of the user's inputs
# CALCULATE totalExpences = amountGas + amountAccomm + amountFood
# CALCULATE finalBalance = amountBudget - totalExpences
# COMMENT: # The over-all expences' amount for the budget for the travel expences
# DISPLAY 'Remaining Balance:', COMPUTE finalBalance/1.0

# END

#
