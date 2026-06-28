import inflect
p = inflect.engine()

name = []

while True:
    try:
        txt = input("Input: ")
        name.append(txt)
    except EOFError:
        break

final = p.join(name)
print("Adieu, adieu, to", final)
