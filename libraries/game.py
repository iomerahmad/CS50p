import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    
    except ValueError:
        pass 
    
number = random.randint(1, level)

while True:
        try:
            guess = int(input("Guess: "))
            if guess == number:
                print("Correct!")
                sys.exit()
            elif guess > number:
                print("Too Big!")
            else:
                print("Too Small!")

        except ValueError:
            pass
        
        



    
