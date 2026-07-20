from PIL import Image, ImageOps
import sys
import os


def main():
    
    if len(sys.argv) == 3:
        if os.path.exists(sys.argv[1]):
            name, extension = os.path.splitext(sys.argv[1])
            extension = extension.lower()
            if extension not in (".jpg", ".jpeg", ".png"):
                sys.exit("Invalid File")
            name_2, extension_2 = os.path.splitext(sys.argv[2])
            extension_2 = extension_2.lower()
            if extension_2 not in (".jpg", ".jpeg", ".png"):
                sys.exit("Invalid File")
            if extension == extension_2:
                shirt = Image.open("shirt.png")
                input_image = Image.open(sys.argv[1])
                resized_input = ImageOps.fit(input_image, shirt.size)
                resized_input.paste(shirt, shirt)
                resized_input.save(sys.argv[2])
            else:
                sys.exit("Both files must have same extension")
        else:
            sys.exit("File does not exists")
    elif len(sys.argv) > 3:
        sys.exit("Too Many command in line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few comand in line arguments")

if __name__ == "__main__":
    main()


    
