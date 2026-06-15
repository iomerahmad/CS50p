def main():
    x, y, z = input("Expression: ").split()
    if y == "+":
        print(f"{float(x)+float(z):.1f}")
    elif y == "-":
        print(f"{float(x)-float(z):.1f}")
    elif y == "*":
        print(f"{float(x)*float(z):.1f}")
    else:
        print(f"{float(x)/float(z):.1f}")
    

main()



