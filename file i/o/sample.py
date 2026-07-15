import sys


def main():
    if len(sys.argv) > 2:
        sys.exit("too many command in line arguments!")
    elif len(sys.argv) < 2:
        sys.exit("Too few command in line argument")
    elif len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            line = 0
            name = sys.argv[1]
            with open(name, "r") as file:
                for lines in file:
                    if lines.lstrip().startswith("#"):
                        pass
                    elif lines.lstrip() == "":
                        pass
                    else:
                        line += 1
        else:
            sys.exit("File not found!")
    print(line)

if __name__ == "__main__":
    main()




    
