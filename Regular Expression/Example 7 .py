import re 
pattern = r"(\d{3})-(\d{2})"
text = "Phone number:123-45"
match = re.search(pattern , text)
print("Area code:", match.group(1))
print("Local code:", match.group(2))