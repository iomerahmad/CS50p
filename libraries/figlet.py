import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid Usage")

if len(sys.argv) == 1:
    random_txt = random.choice(figlet.getFonts())
    figlet.setFont(font=random_txt)

if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("invalid usage")


text = input("Input: ")
print(figlet.renderText(text))










