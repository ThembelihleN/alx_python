letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '@', '&', '(', ')', '*', '+' ]
def validate_password(password):
    characters = letters + numbers + symbols
    password = " ".join(characters)
    for i in range(8):
        return password

    str(input.password(" "))
    if password.length >= 8:
        return True
    else:
        return False
    
validate_password("Password123")
validate_password("abc123")
validate_password("Password 123")
validate_password("password 123")