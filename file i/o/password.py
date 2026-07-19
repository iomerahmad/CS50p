def main():
    while True:
        password = input("Input Password: ")
        result = check(password)
        if result == []:
            print("Valid password ")
            break
        else:
            print(result)


def check(password: str) -> list[str]:
    """Return a list of validation errors; empty list means valid."""
    errors = []
    capital = False
    number = False
    if len(password) >= 8:
        for letter in password:
            if letter.isupper():
                capital = True
            elif letter.isdigit():
                number = True
    if not len(password) >= 8:
        errors.append("Password too short")
    if not capital:
        errors.append("Password must contain atleast 1 capital letter")
    if not number:
        errors.append("Password must contain atleast 1 number")
    return errors
            

if __name__ == "__main__":
    main()

