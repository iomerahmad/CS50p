import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        if len(sys.argv) > 2: 
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            table = list(reader)
            print(tabulate(table, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

main()