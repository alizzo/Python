CountValue = int(input("enter the number of asterisk to display:  "),10) 
mid = int(CountValue // 2)     
for OuterLoop in range(CountValue):
        for innerLoop in range(CountValue):
                if OuterLoop == mid or innerLoop == mid:
                        print("*", end="")
                else:
                        print(" ", end="")
        print()                           

