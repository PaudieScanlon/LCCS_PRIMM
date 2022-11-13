#Name:
#Purpose: A basic population simulator
#Date:

birthRate = 2
deathRate = 0.5
population = 2

for i in range(0,10):
    population = round(population + population*birthRate - population*deathRate)
    print(population)
    
"""
1. Change the code so only the final population is printed to the screen.
2. Change the code so that the user gets to select how many times the loop iterates.
3. By using functions from the random library make the death rate be a
random number between 0 and 1 that is chosen at the beginning of the program.
4. Change the program so that the calculation is within a function called "popModel".
The program should call the function and print the resulting population to the screen.
5. Make the function accept birthRate, deathRate and initial population as inputs
and returns the final population.
6. Have the program include a catastrophe that has a 1 in 20 chance of halving the population.
"""