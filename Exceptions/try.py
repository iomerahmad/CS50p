while True:
    try:
        x = int(input("Whats the numerator? "))
        break
    
    except ValueError:
        print("invalid numerator")
while True:
    try:
         y = int(input("Whats the denominator? "))
         if y == 0:
            print("denominator cant be zero! ")
         else:
             break
    except ZeroDivisionError:
        print("Denominator can't be zero.")


    except ValueError:
        print("Invalid denominator")

print(x/y)
    

   



    

