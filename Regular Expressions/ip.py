


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if int(part) < 0 or int(part) > 255:
            return False
    return True
        
                
if __name__ == "__main__":
    main()