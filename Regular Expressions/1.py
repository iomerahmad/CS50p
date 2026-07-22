import re
username = input("")
def validate_username(username: str) -> bool:
    return(bool(re.search(r"^[a-zA-Z]\w{2,19}$", username)))
print(validate_username(username))