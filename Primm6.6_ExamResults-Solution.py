#Name:
#Purpose: To develop an interactive tool to get stats on student exam results
#Date

#import the necessary libraries
import statistics
import pandas

#open the local CSV file and read in the data to a DataFrame
results_DF = pandas.read_csv("ExamResults.csv")

#create a blank list that will be used to display individual student results
individualResults = []

#4. Ask the user to input which student they would like to see results from and use
#that input to return the appropriate results.
classList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
while True:
    ChosenStudentLetter = input("Which student do you wish to see the results for? Choose one letter from A - J: ").upper()
    if ChosenStudentLetter in classList:
        break

#Choosing the Student we are interested in
ChosenStudent = "Student "+ChosenStudentLetter



#Converting the chosen student's results to a list
individualResults = results_DF[ChosenStudent].tolist()
averageOfResults = statistics.mean(individualResults)
rangeOfResults = max(individualResults) - min(individualResults)

#Printing the chosen student's results to the screen
#1. Add a line of text before the list of results describing what they are.
print("Here are the results for", ChosenStudent)
print(individualResults)
#2. As well as the list of student results, print the average of the set of results.
#with text decribing what it is
print("The average of these results is", averageOfResults)
#3. Print the range of the student results with text decribing what it is.
print("The range of these results is", rangeOfResults)