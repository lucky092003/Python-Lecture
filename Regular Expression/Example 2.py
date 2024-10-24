import re 

pattern = r"[a-z]"
text = "Hello World 123"
match = re.findall(pattern, text)
print("Match found:",match)