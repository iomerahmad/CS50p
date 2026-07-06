def main():
    initial_input = converter()
    if initial_input >= 99:
        print("F")
    elif initial_input <= 1:
        print("E")
    else:
        print(f"{initial_input}%")

def converter():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            if int(x) >= 0 and int(y) != 0 and int(x) <= int(y):
                z = round(int(x)/int(y)*100)
                return z
            
            
            

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        
if __name__ == "__main__":
    main()

        

    

    
        
    