#Name:
#Purpose: A program to calculate energy bills
#Date:

#Setting out variables to be used in the calculation
elecUnits = 100
standingCharge = 2.50
unitCost = 0.13

#Formula to calculate the total cost of electricity for this period
totalCost = elecUnits*unitCost + standingCharge

#Printing the total cost o the screen.
print("Your electricity bill for this period is, €", totalCost)

"""
1. To reflect the energy crisis change the unit cost of electricity to be €0.25 and the standing charge to be €3.95
2. Change the program so that the user is asked to enter how many units of electricity they have used.
Store this information in the elecUnits variable.
3. Add code to the program so the user is asked how much gas units they have used.
Then calculate and print to the screen with a description the cost of the gas.
Use the following information; gas unit cost = €0.08, gas standing charge = €4.95
4. Currently there is a gap between the euro symbol and the numbers. Change the program so there is no gap.
Hint: Only strings can be concatenated.
5. At the moment there is nothing to stop the user entering negative numbers for the amount of electricity used.
Change the program so the user is asked to re-enter the units of electricity if anything other than a positive whole number is entered.
"""