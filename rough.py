def main():
    number = int(input("whats your number?"))
    if is_positive(number):
        print("true")
    else:
        print("false")

   
def is_positive(number: int) -> bool:
    return number > 0

main()



