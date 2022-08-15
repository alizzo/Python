def Calendar():
    Initial_Day = int(input("On what day of the first week should this month start?(0-6):  "))
    Initial_Number_of_Days = int(input("How many days in this month? (28 to 31?):  "))



    DayofMonth = 1
    boxNumber = 0
    SquareWidth = 10
    Days = 7
    NumberLocation = SquareWidth // 2


    while Initial_Day > 6 or Initial_Day < 0 or Initial_Number_of_Days < 28 or Initial_Number_of_Days > 31:
        print("please input a number within the given range...")
        Initial_Day = int(input("What day of the week should this month start?(0-6):  "))
        Initial_Number_of_Days = int(input("How many days in this month? (28 to 31?):  "))
        continue

    else:

        for WeeksInMonth in range(6):    
            
            #Top line
            for VBorder in range(Days):
                if not VBorder:               #responsible for placing the first pipe
                    print("|", end="")
                for HBorder in range(SquareWidth):           #print "----------" (10 hyphens)
                    print("-", end="")
                print("|",end="")                      # after each "----------" print "|" (one Pipe)
            print()



            #Responsible for area inbetween borders & number count   
            for Sidewall in range(3):            # each bored is 3 columns tall
                for OneDay in range(Days):       #
                    if not OneDay:
                        print("|", end="")   #First pipe in vertical border


                  #  if WeeksInMonth > boxNumber or Days > Initial_Day:
                    if Sidewall == 0:
                        if Initial_Day > boxNumber :
                            boxNumber = boxNumber + 1
                            for Spaces in range(SquareWidth):
                                print(" " , end= "")
                            print("|",end="")

                        else:
                            
                            if DayofMonth < 10:

                                #Spaces with numbers
                                for DateValue_and_Spaces in range(SquareWidth):      
                                    if DateValue_and_Spaces == NumberLocation+3:   #number location
                                        print(DayofMonth , end= "")
                                        DayofMonth = DayofMonth + 1 
                                    else:
                                        print(" ", end="")


                            #if the number of days is greater than 10 delete one space
                            elif DayofMonth <= 31 and DayofMonth <= Initial_Number_of_Days:
                                for DateValue_and_Spaces2 in range(SquareWidth-1):
                                    if DateValue_and_Spaces2 == NumberLocation+2:
                                        print(DayofMonth , end= "")
                                        DayofMonth = DayofMonth + 1 
                                    else:
                                        print(" ", end="")
                            else: 
                                for Spaces in range(SquareWidth):
                                    print(" " , end= "")
                                    DayofMonth = DayofMonth + 1          
                            print("|",end="")
                    else:
                            for Hyphen in range(SquareWidth):   #prints the blank during iteration "1" and "2" of sidewall
                                print(" ", end="")
                            print("|",end="")                             
                print()


               
       
        #iterate the last line of boxes          
        for Vborder in range(Days):
            if not Vborder:          #responsible for placing the first pipe of the last line
                print("|", end="")
            for Hborder in range(SquareWidth):           #print "----------" (10 hyphens)
                print("-", end="")
            print("|",end="")               
           
Calendar()


     


     

