def main():
    word = input("input: ")
    print(shorten(word))


def shorten(word: str) -> str:
    """Return word with all vowels removed."""
    result = ""
    for c in word:
        if c.lower() not in "aeiou":
            result += c
    return result


if __name__ == "__main__":
    main()
