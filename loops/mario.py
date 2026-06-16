def main():
    print_square(3)

def print_square(square):
    for i in range(square):
        print_row(square)

def print_row(width):
    print("#" * width)

main()
        


