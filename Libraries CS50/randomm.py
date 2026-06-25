import sys

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("Hello, my name is", sys.argv[1])

    