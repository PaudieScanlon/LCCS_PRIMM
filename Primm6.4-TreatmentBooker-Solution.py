#Name:
#Purpose: To practice basic input and ouput skills with a simple beauty treatement booking system
#Date:

#1. Write a welcome message to the user and ask them to input their name. 
#Store the name in the userName variable

userName = input("Welcome to the beauty treatment booking facility. What is your name? ")

#2. Ask the user their age and store this in an appropriately named variable.
userAge = int(input("What is current age? "))

#3. Ask the user to choose a treament from the following list: Shoulder Massage, Manicure, Pedicure

treatementChoice = int(input("Please choose from the following treatments: \n 1: Shoulder Massage \n 2: Manicure \n 3: Pedicure \n"  ))

if treatementChoice == 1:
    opTreatmentChoice = "shoulder massage"
elif treatementChoice == 2:
    opTreatmentChoice = "manicure"
else:
    opTreatmentChoice = "pedicure"

#4. Ask the user to choose a day and a time for their treatment.
dayChoice = input("What day do you want to have your treatment?\n")
timeChoice = input("What time do you want to have your treatment at?\n")

#5. Display the user's information back to them and ask them to confirm.
print("Thank you", userName+ ". You have chosen a", opTreatmentChoice, "on", dayChoice, "at" , timeChoice +". We look forward to seeing you then.")