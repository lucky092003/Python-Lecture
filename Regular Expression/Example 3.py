import re 

pattern = r"\d{3}"
text = "My number is 1234567890"
match = re.findall(pattern, text)
print("Match found:",match)