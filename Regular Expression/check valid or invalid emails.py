import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)


emails = ["lucky123@gmail.com", "lucky-123-email.com",]

for email in emails:
    if validate_email(email):
        print(f"{email} is valid.")
    else:
        print(f"{email} is invalid.")


