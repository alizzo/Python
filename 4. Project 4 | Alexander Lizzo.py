def box():              #this creates a function called box -- I learned it from the text book written by John Zelle in chapter 1. After this program has been run - the user can call the function "box()" to re-reun the code - it's helpful in the debugging stages
    CountValue = int(input("enter the number of asterisk to display:  "),10)  #Use input and int functions to get a count value, from the user that is running the program.
    mid = float(((CountValue/2)-(1/2)))      # (also you can use // to divide intergers & it will discard remainder --- The variable "mid" stores one half of the user input as a floating point integer less .5 -- this variable is only call in the case where the user input is odd -- this statement helps to determine the mid point. 

    for OuterLoop in range(CountValue):    # iterate the iteration
        if CountValue%2 == 1:             # use modulus to determine if the user input is odd (since the input is set to 1 if input is odd this statement is True)
            for innerLoop in range(CountValue):  # "inner" iteration loop that will print the range specified by user (stored in variable CountValue) 
                if OuterLoop < int(mid):          # if the value of the outerloop is less than the mid statement print stars
                    print("*", end='')
                elif OuterLoop > int(mid):         #if the value of the outerloop is greater than the mid statement print stars
                    print("*", end='')
                elif OuterLoop and innerLoop == int(mid) :   # now if the value of the outer & inner loop are the "mid" value print "O"
                    print("O", end='')
                else:
                    print("*", end='')                # if the value is anything else print stars 
            
        else:                             # use modulus to determine if the user input value is other than odd (determine if even)
            for innerLoop in range(CountValue):
                print("*", end='')  
        print()                              # \n breakline -- default print statement behavior; break line before print the next line of stars
box()







