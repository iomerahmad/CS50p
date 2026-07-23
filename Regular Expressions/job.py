import re
import sys


def main():
    s = input("Hours: ")
    final = convert(s)
    print(final)


def convert(s):
    entry = re.search(r"^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{2}))?\s(AM|PM)$", s)
    if not entry:
        raise ValueError("Invalid Format!")
    hour1 = int(entry.group(1))
    minute1 = entry.group(2)
    meridiem1 = entry.group(3)
    hour2 = int(entry.group(4))
    minute2 = entry.group(5)
    meridiem2 = entry.group(6)

    if not (1 <= hour1 <= 12) or not (1 <= hour2 <= 12):
        raise ValueError("Invalid hour")

    if minute1 is None:
        minute1 = 0
    else:
        minute1 = int(minute1)
        if not (0 <= minute1 <= 59):
            raise ValueError("Invalid minute")

    if minute2 is None:
        minute2 = 0
    else:
        minute2 = int(minute2)
        if not (0 <= minute2 <= 59):
            raise ValueError("Invalid minute")

    if meridiem1 == "AM" and hour1 == 12:
        hour1 = 0
    if meridiem1 == "PM" and hour1 != 12:
        hour1 += 12
    if meridiem2 == "AM" and hour2 == 12:
        hour2 = 0
    if meridiem2 == "PM" and hour2 != 12:
        hour2 += 12

    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"


if __name__ == "__main__":
    main()