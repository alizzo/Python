grade1 = float(input("give me a number: "))
grade2 = float(input("give me a number: "))
grade3 = float(input("give me a number: "))  #accepts three values from the user, converts each to float, and stores the values in three variables.

average = (grade1 + grade2 + grade3)/3  #step 2 & 3: Assign the addition of the these three variables into a third ‘sum’ variable & Calculate the average of the three numbers
print(average)   #step 3 print out average

if average >= 90:
    print("Final grade is an A")        #If the average of the three numbers >= 90.0 the program should print the text string ‘Final grade is an A’
elif average >= 80:
    print("Final grade is a B’")  #If not an ‘A’, and if the average of the three numbers >= 80.0 the program should print the text string ‘Final grade is a B’
elif average >= 70:
    print("Final grade is a C")   #If not an ‘A’ or a ‘B’, and if the average of the three numbers >= 70.0 the program should print the text string ‘Final grade is a C’
elif average >= 60:
    print("Final grade is a D")   #If not an ‘A’, ‘B’, or a ‘C’, and if the average of the three numbers >= 60.0 the program should print the text string ‘Final grade is a D’
else:
    print("Ooops, please work harder") # If not an ‘A’, ‘B’, ‘C’, or a ‘D’ the program should print the text string ‘Ooops, please work harder’
