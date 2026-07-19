def main():
    while True:
        password = input("Input Password: ")
        result = check(password)
        if result == True:
            print("Valid password ")
            break
        elif result == "Password must contain atleast 1 capital letter":
            print("Password must contain atleast 1 capital letter")
        elif result == "Password must contain atleast 1 number":
            print("Password must contain atleast 1 number")
        elif result == "Password too short":
            print("Password too short")

def check(password: str) -> bool | str:
    if len(password) >= 8:
        capital = False
        number = False
        for letter in password:
            if letter.isupper():
                capital = True
            elif letter.isdigit():
                number = True
        if capital and number:
            return True
        if not capital:
            return "Password must contain atleast 1 capital letter"
        if not number:
            return "Password must contain atleast 1 number"
    else:
        return "Password too short"

            
            

if __name__ == "__main__":
    main()