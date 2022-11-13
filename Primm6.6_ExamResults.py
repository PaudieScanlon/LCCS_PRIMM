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

studentNumber = "Student A" 

individualResults = results_DF[studentNumber].tolist()

print(individualResults)

"""
1. Add a line of text before the list of results describing what they are.
2. As well as the list of student results, print the average of the set of results.
with text decribing what it is.
3. Print the range of the student results with text decribing what it is.
4. Ask the user to input which student they would like to see results from and use
that input to return the appropriate results.
"""