MaxCount = int(input("enter first a number:  "))   #Use input and int functions to get a maximum count value, from the user that is running the program.  You can pick the variable name.
#MaxCount = int(MaxCount, 10) -->    #Create a second variable to hold an iteration count value.  The iteration count variable will be used to control how many times the loop executes.  You can also select the name of this variable.

OuterCount = 0                         # Assign the iteration count variable a starting value of 0.
while OuterCount < MaxCount:             #Write a while statement that contains a condition (i.e. outerCount < maxCount) that will have the program continue iterating in the while loop as long as iteration count is less than the maximum count.
        innerCount = 0
        while innerCount < MaxCount:
            print('*', end='')            #Inside the loop add a statement to print one asterisk and not break to the next line ( end='' ); end='' replaces default behavior with nonspace
            innerCount = innerCount +1    # increments asterix from 0 to some number, based on users input
        print()                           #default behavior is to break line (\n) -- therefore this print statement creates a page break
        OuterCount = OuterCount +1         #Make sure you increment the iteration count variable inside the while loop, or you may end up with an endless loop.
       
