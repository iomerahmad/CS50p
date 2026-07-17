import csv
import sys


def main():
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    try:
        with open(sys.argv[1]) as in_file, open(sys.argv[2], "w") as out_file:
            reader = csv.DictReader(in_file)
            writer = csv.DictWriter(out_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


main()