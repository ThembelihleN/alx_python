import re
def validate_password(password):
   
    if len(password) < 8:
        return False
    if not re.search('[a-z]', password):
        return  False
    if not re.search('[A-Z]', password):
        return  False
    if not re.search('[0-9]', password):
        return  False
    else:
        return True
    
(validate_password("Password123"))
validate_password("abc123")
validate_password("Password 123")
validate_password("password 123")