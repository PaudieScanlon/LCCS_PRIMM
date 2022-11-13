#Name:
#Purpose: A basic population simulator
#Date:

import random
import csv

birthRate = 2

#3. By using functions from the random library make the death rate be a
# random number between 0 and 1 that is chosen at the beginning of the program.
deathRate = random.randint(0,10)*0.1
population = 2

#2. Change the code so that the user gets to select how many times the loop iterates.
cycles = int(input("How many times do you want the simulation to run? "))

#4. Change the program so that the calculation is within a function called "popModel".
# The program should call the function and print the resulting population to the screen.

def popModel(initPop):
    with open("population.csv", "w") as f:
        for i in range(0,cycles):
            initPop = round(initPop + initPop*birthRate - initPop*deathRate)
            catastrophe = random.randint(1,20)
            f.write("%d" % initPop "\n")
            if catastrophe == 1:
                initPop = initPop/2
            
#1. Change the code so only the final population is printed to the screen.

print(popModel(population))
    
"""

5. Have the program include a catastrophe that has a 1 in 20 chance of halving the population.
"""