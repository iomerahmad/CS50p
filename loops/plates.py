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
        
        


main()
