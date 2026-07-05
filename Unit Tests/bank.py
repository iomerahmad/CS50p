def main():
    greeting = input("Greeting: ").lstrip().lower()
    print(value(greeting))


def value(greeting):
    if greeting.lstrip().lower().startswith("hello"):
        return "$0"
    elif greeting.lstrip().lower().startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()

