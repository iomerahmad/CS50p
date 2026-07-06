def main():
    fraction = input("Fraction: ")
    x, y = convert(fraction)
    percent = gauge(x, y)

    print(format_output(percent))


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)

    if y == 0 or x > y:
        raise ValueError

    return x, y


def gauge(x, y):
    return round(x / y * 100)


def format_output(percent):
    if percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()
        

    

    
        
    