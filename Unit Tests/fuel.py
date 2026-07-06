def main():
    x, y = converter()
    percent = gauge(x, y)

    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")


def converter():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)

            if 0 <= x <= y and y != 0:
                return x, y
        except ValueError:
            pass


def gauge(x, y):
    return round(x / y * 100)


if __name__ == "__main__":
    main()
        

    

    
        
    