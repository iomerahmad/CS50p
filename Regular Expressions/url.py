import re
import sys


def main():
    HTML = input("URL: ")
    print(parse(HTML))


def parse(HTML):
    match = re.search(r"https?://(www\.)?youtube\.com/embed/(\w+)", HTML)
    if match:
        return f"https://youtu.be/{match.group(2)}"
    else:
        return None


if __name__ == "__main__":
    main()