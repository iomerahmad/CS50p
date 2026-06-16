def main():
    meow(get_number())
    

def get_number():
    while True:
        n = int(input("Whats your number? "))
        if n>0:
            return n
        
    

def meow(n):
    for _ in range(n):
        print("meow")


main()

