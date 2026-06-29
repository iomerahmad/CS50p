import random


def main():
    level = get_level()
    score = 0
    
    for _ in range(10):
        rand_1 = generate_integer(level)
        rand_2 = generate_integer(level)
        answer = rand_1 + rand_2
    
        for attempt in range(3):
            try:
                user_answer = int(input(f"{rand_1} + {rand_2} = "))
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{rand_1} + {rand_2} = {answer}")
    print(f"score: {score}/10")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError(f"Invalid Level, {level}")




if __name__ == "__main__":
    main()
