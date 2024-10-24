import re

def is_strong_password(password):

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@()!%?&])[A-Za-z\d@()!%?&]{8,}$'
    

    return re.match(pattern, password) is not None

print(is_strong_password("Lucky@822"))  
print(is_strong_password("lucky822"))      


