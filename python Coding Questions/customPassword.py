#  4. Custom Password Validator 
# Rules: 
# • Min 8 chars  
# • At least 1 uppercase, 1 lowercase, 1 digit 
# Use:  
# • string operations  
# • loops + conditionals  
# • Raise custom exception if invalid 

class PasswordError(Exception):
    pass

# function to check validate password or not
def validate_password(password):

    # length should be greater than 8 characters
    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    # if not contain uppercase, lowercase, and digit
    if not (has_upper and has_lower and has_digit):
        raise PasswordError("Password must contain uppercase, lowercase, and digit")

    # else contain 
    return True

# Example
try:
    validate_password("Abc12345")
    print("Valid Password")
except PasswordError as e:
    print(e)