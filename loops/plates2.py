def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if 6 < len(plate) or len(plate) < 2 :
        return False
    elif not plate[0].isalpha() or not plate[1].isalpha():
        return False
    elif not plate.isalnum():
        return False
    number_started = False
    for c in plate:
        if not number_started and c == "0":
            return False
        if c.isdigit():
            number_started = True
        if number_started and c.isalpha():
            return False
    return True
        
    

if __name__ == "__main__":
    main()

        
            
        
    
        
    

    

        
        


main()
