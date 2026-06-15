def main():
    time  = input("what time is it? ")
    if 7 <= convert(time) <= 8:
        print("Breakfast time")
    elif 12 <= convert(time) <= 13:
        print("Lunch time")
    elif 18 <= convert(time) <= 19:
        print("Dinner time")
    

def convert(time):
    h, m = time.split(":")
    m_final = int(h) + int(m)/60
    return m_final



if __name__ == "__main__":
    main()
