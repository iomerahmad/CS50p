def main():
    text = input("input: ")
    for c in text:
        if c.lower() not in "aeiou":
            print(c, end="")
    print()
if __name__ == "__main__":
    main()

        
    



