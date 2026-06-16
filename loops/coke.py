due = 50

while due > 0:
    insertion = int(input("Insert coin: "))
    if insertion == 25:
        due = (due - 25)
        if due > 0:
            print("amount due", due)
        
    elif insertion == 10:
        due = due - 10
        if due > 0:
            print("amount due", due)
        
    elif insertion == 5:
        due = due - 5
        if due > 0:
            print("amount due", due)
        
    else:
        print("due amount", due)
print("change: ", abs(due))
